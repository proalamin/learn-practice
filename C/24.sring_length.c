#include <stdio.h>
#include <string.h>

int main(){

    // find string length through for loop
    char str[20]="abcde efg";
    int length=0;
    for(int i=0; str[i] != '\0'; i++){
        length++;
    }
    printf("%d\n", length);


    // find string length through library function
    char name[20]="al amin";
    int nameLength=strlen(name);
    printf("%d\n", nameLength);

}