#include<stdio.h>

int main(){

    char str[50];

    //input
    // scanf("%[^\n]s", str);
    fgets(str, sizeof(str), stdin);


    // output
    fputs(str, stdout);
    // printf("%s", str);

    

    return 0;
}