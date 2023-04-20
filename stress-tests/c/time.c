#include <time.h>
#include <stdio.h>

int main() {

    time_t ts;
    time( &ts );
    printf("%ld", ts);
    return 0;
}