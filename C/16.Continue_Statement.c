/*
100 to 300 number print the all number which is divisible by 2,3,5 
*/


#include <stdio.h>

int main(){

    for(int i=100; i<=300; i++){

        // printf("checking %d\n", i);

        if(i%2==0 && i%3==0 && i%5==0){
            printf("%d is this number\n", i);
            continue;
        }
        printf("%d is not number\n", i);
    }

    return 0;
}