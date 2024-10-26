#include<stdio.h>
#include<string.h>

int main(){
    char str[20]="al amin";

    char str2[20];
    strcpy(str2, str);

    int length=strlen(str);

    for(int i=0, j=length-1; i<=j; i++, j--){
        char temp= str[i];
        str[i]=str[j];
        str[j]=temp;
    }
    printf("%s %s",str2, str);


    // library function
    // strrev(str); // not works all compiler
    // printf("%s", str);



}