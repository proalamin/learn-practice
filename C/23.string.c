#include<stdio.h>

int main(){

    char str[50];

    //input
    // scanf("%[^\n]s", str);
    fgets(str, sizeof(str), stdin);


    // output
    // printf("%s", str);
    fputs(str, stdout);

    
    //Converting String to Integer Number
    char con[20];
    int n; // size

    scanf("%d", &n);
    scanf("%s", con);

    int num=0;
    for(int i=0; i<n; i++){
        int digit=con[i]-'0';

        num=num * 10 + digit;
    }
    printf("%d", num);

    return 0;
}