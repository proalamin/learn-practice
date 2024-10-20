#include <stdio.h>

int a[10000];
int b[10000];

int main(){
    int length;
    scanf("%d", &length);

    for(int i=0; i<length; i++){
        scanf("%d", &a[i]);
    }

    // reverse and a to b
    for(int i=0, j=length-1; i<length; i++, j--){
        b[j]=a[i];
    }

    // again b to a
    for(int i=0; i<length; i++){
        a[i]=b[i];
    }

    for(int i=0; i<length; i++){
        printf("%d ", a[i]);
    }

}