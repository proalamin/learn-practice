#include<stdio.h>

int main(){
    int a=5;
    int *b= &a;
    printf("%d %d\n", &a, b);


    int arr[5]={1,2,3,4,5};
    int *p=&arr;
    printf("%d %d\n", &arr[0], p);
    printf("%d", (p+3));

    return 0;
}