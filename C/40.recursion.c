#include<stdio.h>


// x to n
void fun(int x, int n){
    if(x>n){
        return;
    }
    printf("%d ", x);
    fun(x+1, n);
}

// n to 1
void fun2(int n){
    if(n==0){
        return;
    }
    printf("%d ", n);
    fun2(n-1);

}

// array sum
int a[100000], sum;
void goTOIndex(int i, int n){
    if(i == n){
        return;
    }
    sum +=a[i];

    goTOIndex(i+1, n);

}

int main(){
    int n=5;
    int x=1;
    fun(x, n);
    printf("\n");
    fun2(n);
    printf("\n");

    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    sum=0;
    goTOIndex(0, n);
    printf("%d", sum);

}