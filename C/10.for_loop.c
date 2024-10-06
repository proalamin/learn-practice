/*
for(initialization; condition; update){
        statement
    }
*/

#include <stdio.h>

int main(){
    
    // print  1 to 10 (here i start 1 and continue 10<+)
    for(int i=1; i<=10; i++){
        printf("value of i= %d\n", i);
    }
    printf("outside for loop\n");

    return 0;
}