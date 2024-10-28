#include<stdio.h>

int main(){
    int a[100000];
    int len;
    scanf("%d", &len);

    for(int i=0; i<len; i++){
        scanf("%d", &a[i]);
    }

    int delIndex;
    scanf("%d", &delIndex);

    if(delIndex<0 || delIndex>=len){
        printf("index not dave this array");
    }

//0 1 2 3 -index
//1 2 3 4
//1 2 4

    for(int i=delIndex; i<len-1; i++){
        a[i]=a[i+1];
    }

    len--;
    for(int i=0; i<len; i++){
        printf("%d ", a[i]);
    }


    return 0;
}