#include <string>
#include <chrono>
#include <iostream>


int main(){
    using namespace std::chrono;
    auto begin = high_resolution_clock::now();
    uint64_t ms = duration_cast<milliseconds>(begin.time_since_epoch()).count();
    std::string ms_conv = std::to_string(ms);
    int decloc = ms_conv.size() - 3;
    ms_conv.insert(decloc, ".");
    std::cout << ms_conv << "\n";
    
}