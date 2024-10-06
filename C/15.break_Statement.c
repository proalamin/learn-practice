/*
100 to 300 number print the first number which is divisible by 2,3,5 
*/

#include <stdio.h>

int main(){

    for(int i=100; i<=300; i++){

        // printf("checking %d\n", i);

        if(i%2==0 && i%3==0 && i%5==0){
            printf("%d is this number\n", i);
            break;
        }
    }

    return 0;
}