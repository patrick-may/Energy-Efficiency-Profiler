#include <time.h>
#include <stdio.h>

int main() {
    clock_t ts = clock();

    for(size_t i = 0; i < 100000; ++i){
        ++i;
    }
    clock_t te = clock();
    printf("%ld%ld",ts,te);
}