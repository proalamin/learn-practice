#include<stdio.h>

int main(){
    int a[100000], b[100000];

    int len1=0, len2=0;
    scanf("%d", &len1);

    for(int i=0; i<len1; i++){
        scanf("%d", &a[i]);
    }

    printf("before COPY\n");
    for(int i=0; i<len1; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    for(int i=0; i<len1; i++){
        printf("%d ", b[i]);
    }


    printf("\n");
    printf("AFTER COPY\n");
    for(int i=0; i<len1; i++){
        b[i]=a[i];
    }
    len2=len1;
    for(int i=0; i<len2; i++){
        printf("%d ", b[i]);
    }


    return 0;
}