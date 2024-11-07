#include<stdio.h>

int add(int a, int b){
    int sum=a+b;
    return sum;
}


// void function ->when need print result
void aplhaCheck(char input){
    if('a'<= input && input<='z'){
        printf("Lower\n");
    }else{
        printf("Upper\n");
    }
}


int main(){
    int x, y;
    scanf("%d %d", &x, &y);

    int result= add(x,y);
    printf("%d\n", result);

    aplhaCheck('a');
    aplhaCheck('A');

    return 0;
}