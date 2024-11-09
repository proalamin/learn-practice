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

int main(){
    int n=5;
    int x=1;
    fun(x, n);
    printf("\n");
    fun2(n);

}