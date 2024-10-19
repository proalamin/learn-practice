#include <stdio.h>
#include<limits.h>


int main(){ 

    //array declaration
    int a[5]={1,3,4,2,7};

    int b[5]={2,5}; // b[5]={2,5,0,0,0};

    int c[]={3,5}; // here array size is 2

    // array input output
    int n[5];

    for(int i=0; i<5; i++){
        scanf("%d", &a[i]);
    }

     for(int i=0; i<5; i++){
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
    printf("avg- %llf\n", avg);


    // min and max
    int d[7]={3,5,9,3,2,1,8};

    int min= INT_MAX, max=INT_MIN;

    for(int i=0; i<7; i++){
        if(d[i] < min){
            min=d[i];
        }

        if(d[i] > max){
            max=d[i];
        }
    }
    printf("min - %d\nmax- %d", min,max);


    return 0;
}