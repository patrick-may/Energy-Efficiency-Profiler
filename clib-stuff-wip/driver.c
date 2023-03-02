#include <stdio.h>
#include "PowerLog3.0/IntelPowerGadgetLib.h"

int main(int argc, char** argv){
    
    int bef = rapl_before();
    int aft = rapl_after();
    printf("%i, %i",bef, aft);
    return 0;
}

