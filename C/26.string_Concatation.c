#include <stdio.h>
#include <string.h>

int main(){
    char a[20]="hello ";
    char b[20]="world ";

    // marge a then b=a
    strcat(a, b);
    printf("%s\n", a);

    // marge b then a=b
    strcat(b, a);
    printf("%s", b); // output- world hello world (bcz already a then b marge then b to a)



}