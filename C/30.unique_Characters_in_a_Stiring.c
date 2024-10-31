#include<stdio.h>
#include<string.h>

int main(){
    char str[100]="apple";

    int f[26]={0};

    int len=strlen(str);

    for(int i=0; i<len; i++){
        char ch= str[i];
        int index= ch-'a';
        f[index]=1;
    }

    int count=0;
    for(int i=0; i<26; i++){
        // printf("%c %d\n", i+'a', f[i]); //this is print which char have all alphabet

        count += f[i];

        if(f[i]==1){
            printf("%c %d\n", i+'a', f[i]); // which unique char have this string
        }
    }

    printf("%d", count); //how much unique char have this string



    
    return 0;
}