#pragma once

#include <string>
#include <chrono>
#include <iostream>
#include <fstream>

#define COWPROF_FILEPATH "data/intervals/c++/TimeLog-2023-04-20-10-09-17.659270.csv"

using namespace std::chrono;

class CowLog {

    public:
        std::string funcname;
        uint64_t begms;
        uint64_t endms;

        CowLog(std::string fname){
            funcname = fname;
            begms = duration_cast<milliseconds>(high_resolution_clock::now().time_since_epoch()).count();
        }

        void finish(){
            endms = duration_cast<milliseconds>(high_resolution_clock::now().time_since_epoch()).count();
            std::string writeme = funcname + ',' + conv(begms) + ',' + conv(endms) +'\n';
            std::ofstream outfile;
            outfile.open(COWPROF_FILEPATH, std::ios::app);
            outfile << writeme;
            outfile.clear();
        }

    private:
        std::string conv(uint64_t ms){
            std::string ms_conv = std::to_string(ms);
            int decloc = ms_conv.size() - 3;
            ms_conv.insert(decloc, ".");
            return ms_conv;
        }
};