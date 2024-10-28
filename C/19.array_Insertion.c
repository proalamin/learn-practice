#include<stdio.h>

int main(){
    int a[100000], b[100000];
    int len;
    scanf("%d", &len);

    for(int i=0; i<len; i++){
        scanf("%d", &a[i]);
    }

//1 2 3 4
//2 30 ->hear 2 index and value 30
//1 2 30 3 4 

    int index,value;
    scanf("%d %d", &index, &value);

    len++;
    for(int i=len-1; i>=index; i--){
        a[i+1]=a[i];
    }
    a[index]=value;

    
    for(int i=0; i<len; i++){
        printf("%d ", a[i]);
    }

    return 0;
}