/*
Copyright (c) (2013) Intel Corporation All Rights Reserved.

The source code, information and material ("Material") contained herein is owned by Intel Corporation or its suppliers or licensors, and title to such Material remains with Intel Corporation or its suppliers or licensors. The Material contains proprietary information of Intel or its suppliers and licensors. The Material is protected by worldwide copyright laws and treaty provisions. No part of the Material may be used, copied, reproduced, modified, published, uploaded, posted, transmitted, distributed or disclosed in any way without Intel's prior express written permission. No license under any patent, copyright or other intellectual property rights in the Material is granted to or conferred upon you, either expressly, by implication, inducement, estoppel or otherwise. Any license under such intellectual property rights must be express and approved by Intel in writing.


Include any supplier copyright notices as supplier requires Intel to use.

Include supplier trademarks or logos as supplier requires Intel to use, preceded by an asterisk. An asterisked footnote can be added as follows: *Third Party trademarks are the property of their respective owners.

Unless otherwise agreed by Intel in writing, you may not remove or alter this notice or any other notice embedded in Materials by Intel or Intel’s suppliers or licensors in any way.
*/

// PowerLog3.0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "IntelPowerGadgetLib.h"

static TCHAR *g_szProgName = NULL;
static unsigned int g_duration = 0;
static unsigned int g_resolution = 100;
static TCHAR *g_szLogfile = L"PowerLog.csv";
static TCHAR g_szCmd[256];
static bool g_verbose = false;
static volatile bool g_finish = false;

static DWORD ThreadFunc (LPVOID lpdwThreadParam )
{
	BOOL bSuccess = FALSE;
	if (g_szCmd[0] == NULL)
	{
		Sleep(g_duration);
	}
	else 
	{
		STARTUPINFOW siStartupInfo; 
		PROCESS_INFORMATION piProcessInfo; 
		memset(&siStartupInfo, 0, sizeof(siStartupInfo)); 
		memset(&piProcessInfo, 0, sizeof(piProcessInfo)); 
		siStartupInfo.cb = sizeof(siStartupInfo); 

		bSuccess = ::CreateProcess(NULL, g_szCmd, 0, 0, FALSE,CREATE_DEFAULT_ERROR_MODE,0, 0, &siStartupInfo, &piProcessInfo);
		if (bSuccess)
		{
			::WaitForSingleObject (piProcessInfo.hProcess, INFINITE);
			::CloseHandle(piProcessInfo.hProcess);
			::CloseHandle(piProcessInfo.hThread);
		}
	}

	g_finish = true;

	return 0;
}

void printHelp()
{
	printf("Usage: \n");
	printf("log power data to logfile for a period of time:\n");
	printf("\tPowerLog.exe [-resolution <msec>] -duration <sec> [-verbose] [-file <logfile>]\n");
	printf("start a command and log power data to logfile until the command finish\n");
	printf("\tPowerLog.exe [-resolution <msec>] [-file <logfile>] [-verbose] -cmd <command>\n");
	printf("Default for resolution = 100 ms\n");
	printf("Default for logfile = PowerLog.csv\n");
	printf("-cmd must be the last parameter\n");
}

void cmdLine(int argc, _TCHAR **argv)
{
	g_szProgName = argv[0];

	if (argc < 2) {
		printHelp();
		_exit(0);
	}

	int i = 1;
	g_szCmd[0] = NULL;

	while (i < argc)
	{

		if (wcscmp(argv[i],L"-duration") == 0)
		{
			i++;
			g_duration = _wtoi(argv[i++]) * 1000;
		}
		else if (wcscmp(argv[i],L"-verbose") == 0)
		{
			g_verbose = true;
			i++;
		}
		else if (wcscmp(argv[i], L"-resolution") == 0)
		{
			i++;
			g_resolution = _wtoi(argv[i++]);
		}
		else if (wcscmp(argv[i],L"-file") == 0)
		{
			i++;
			g_szLogfile = argv[i++];
		}
		else if (wcscmp(argv[i],L"-cmd") == 0)
		{
			i++;
			TCHAR *pChar = g_szCmd;
			for (int j = i; j < argc; j++)
			{
				wcscpy_s(pChar,256, argv[i]);
				pChar += wcslen(argv[i++]);
				*pChar++ = L' ';
			}
			pChar--;
			*pChar = NULL;
		}
		else if (wcscmp(argv[i],L"-help") == 0)
		{
			printHelp();
			_exit(0);
		}
		else
		{
			printHelp();
			_exit(-1);
		}

	}

	if (g_szCmd[0] == NULL && g_duration == 0)
	{
		printf("Either specify duration or cmd\n");
		printHelp();
		_exit(-1);
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	CIntelPowerGadgetLib energyLib;
	bool bSuccess = false;

	// Parse cmd line
	cmdLine(argc, argv);

	// Initialize the driver & library
	if (energyLib.IntelEnergyLibInitialize() == false)
	{
		wprintf(L"Error: %s\n", energyLib.GetLastError());
		return -1;
	}

	int maxTemp = 0, temp = 0;
	int currentNode = 0;

	if (energyLib.GetMaxTemperature(currentNode, &maxTemp))
		wprintf(L"Max Temp = %d\n", maxTemp);

	int numNodes = 0; 
	if (energyLib.GetNumNodes(&numNodes))
		wprintf(L"number of nodes = %d\n", numNodes);

	int numMsrs = 0;
	energyLib.GetNumMsrs(&numMsrs);

	// Report TDP.
	for (int i = 0; i < numNodes; i++)
	{
		double TDP;
		if (energyLib.GetTDP(i, &TDP))
			wprintf(L"TDP(mWh)_%d = %5.2f\n", i, TDP);
	}

	double baseFrequency;
	if (energyLib.GetBaseFrequency(currentNode, &baseFrequency))
		wprintf(L"Base Frequency = %6.2f(MHz)\n", baseFrequency);

	wprintf(L"Logging...");
	g_finish = false;

	::CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE) ThreadFunc, NULL, 0, NULL);

	energyLib.StartLog(g_szLogfile);
	while (g_finish == false)
	{
		Sleep(g_resolution);

		if (energyLib.ReadSample() == false)
			wprintf(L"Warning: %s\n", energyLib.GetLastError());

		if (g_verbose == true)
		{
			if(energyLib.IsGTAvailable())
			{
				int freqGT = 0;
				energyLib.GetGTFrequency(&freqGT);
				wprintf(L"GT Frq = %5d\n", freqGT);
			}

			for (int j = 0; j < numMsrs; j++)
			{
				int funcID;
				energyLib.GetMsrFunc(j, &funcID);
				double data[3];
				int nData;
				wchar_t szName[MAX_PATH];

				energyLib.GetPowerData(currentNode, j, data, &nData);
				energyLib.GetMsrName(j, szName);

				// Frequency
				if (funcID == 0)
				{
					wprintf(L"%s Frq = %5.0f\n", szName, data[0]);
				}
				// Power
				else if (funcID == 1)
				{
					wprintf(L"%s power (W) = %6.2f\n", szName, data[0]);
					wprintf(L"%s energy (J) = %6.2f\n", szName, data[1]);
					wprintf(L"%s energy (mWh) = %6.2f\n", szName, data[2]);
				}
				// Temperature
				else if (funcID == 2)
				{
					wprintf(L"%s temperature (C) = %6.0f\n", szName, data[0]);
					wprintf(L"%s Hot = %3.0f\n", szName, data[1]);
				}
				else if (funcID == 3)
				{
					wprintf(L"%s power limit (W) = %6.2f\n", szName, data[0]);
				}
			}
			wprintf(L"--------------------------\n");
		}
	}
	energyLib.StopLog();
	wprintf(L"Done\n");

	return 0;
}
