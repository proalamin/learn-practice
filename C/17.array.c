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

    printf("\n");

    // sum of an array
    int x;
    scanf("%d", &x);

    int y[x];

    for(int i=0; i<x; i++){
        scanf("%d", &y[i]);
    }

    int sum=0;
    for(int i=0; i<x; i++){
        sum +=a[i];
    }
    printf("array sum answer is- %d\n", sum);

    double avg = (double)sum / x;
    printf("avg- %llf", avg);

    return 0;
}