#include<stdio.h>
// 4 5
// out- 5 6 (using function)

void swap(int *x, int *y){
    int temp=*x;
    *x=*y;
    *y=temp;
}


int main(){
    int a=4, b=5;

    printf("before swap- %d %d\n", a,b);

    swap(&a, &b);

    printf("after swap- %d %d\n", a,b);


    return 0;
}