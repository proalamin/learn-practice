/*
for(initialization; condition; update){
        statement
    }
*/

#include <stdio.h>

int main(){
    
    // print to 1 to 10 
    for(int i=1; i<=10; i++){
        printf("value of i= %d\n", i);
    }
    printf("outside for loop\n");

    return 0;
}