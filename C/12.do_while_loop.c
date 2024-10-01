/*
do while loop-

initialization
do{
.......
.......
increment/decrement;
}while(condition);
*/

#include <stdio.h>

int main(){
    int i=0;
    do{
        printf("inside do while loop\n");
        i++;
    }while(i<=3);
    printf("outside do while loop\n");


    return 0;
}