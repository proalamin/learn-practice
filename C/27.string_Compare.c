#include <stdio.h>
#include <string.h>

/*
0->[a=b]
<0->[a<b]
>0->[a>b]

*/

int main(){
    char a[50]="air";
    char b[50]="apple";

    int cmp = strcmp(a, b);
    printf("%d", cmp);


}