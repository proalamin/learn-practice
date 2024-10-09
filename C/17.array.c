#include <stdio.h>

int main(){ 

    //array declaration
    int a[5]={1,3,4,2,7};

    int b[5]={2,5}; // b[5]={2,5,0,0,0};

    int c[]={3,5}; // here array size is 2

    // array input output
    int n[5];

    for(int i=0; i<5; i++){
        scanf("%d", &a[i]);
        printf("%d ", a[i]);
    }


    return 0;
}