#include <bits/stdc++.h>
#include <unistd.h>

#include "wrapper.hpp"

using namespace std;


void snooze(){
    CowLog s("snooze");
        
    sleep(10);

    s.finish();
}

void thrash(){
    CowLog s("thrash");

    long long int ct = 0;
    for(long long int i = 0; i < 1000000000; ++i){
        ct += 1;
    }

    s.finish();
}
int main() {
    cout << "thonk time 🤬" << "\n";
    for(int i = 0; i < 10; ++i){
        if(i % 2){
            thrash();
        }
        else{
            snooze();
        }
    }
}