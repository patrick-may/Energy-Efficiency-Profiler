#pragma once

#include <string>
#include <chrono>
#include <iostream>
#include <fstream>

#define COWPROF_FILEPATH "data/intervals/c++/TimeLog-2023-04-22-16-02-22.819401.csv"

class CowLog {

    public:
        std::string funcname;
        uint64_t begms;
        uint64_t endms;

        // timestamp beginning of spot of interest
        CowLog(std::string fname){
            funcname = fname;
            begms = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now().time_since_epoch()).count();
        }

        // timestamp end, append entire instance info
        void finish(){
            endms = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now().time_since_epoch()).count();
            std::string writeme = funcname + ',' + conv(begms) + ',' + conv(endms) +'\n';
            std::ofstream outfile;
            outfile.open(COWPROF_FILEPATH, std::ios::app);
            outfile << writeme;
            outfile.close();
        }

    private:
        // hack to transform millisecond since epoch to string of seconds since epoch
        std::string conv(uint64_t ms){
            std::string ms_conv = std::to_string(ms);
            int decloc = ms_conv.size() - 3;
            ms_conv.insert(decloc, ".");
            return ms_conv;
        }
};