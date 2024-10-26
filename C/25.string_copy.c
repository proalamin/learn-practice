#include <stdio.h>
#include <string.h>

int main(){

    char a[10]="def";
    char b[10]="abcdef";

    // strcpy(destination, source);
    strcpy(a, b);

    printf("%s %s", a, b);

}