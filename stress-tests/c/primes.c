#include <stdio.h>
#include <stdbool.h>

#define N 100000

bool is_prime(int n){
    for (size_t i = 2; i < n; ++i){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}
int main(){
    for(int i = 2; i < N; ++i){
        if (is_prime(i)){
            printf("%i ", i);
        }
    }
    printf("\n");
    return 0;
}