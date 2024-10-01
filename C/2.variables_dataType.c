
/*
formate specifire

short int %hd
int %d
long int %ld
long long int %lld
char %c
float %f
double %lf
long double %Lf

unsigned int %u
unsigned short %hu
unsigned long int %lu
unsigned long long int %llu

*/



#include <stdio.h> 

int main(){
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    printf("a= %d b= %d c= %d d= %d", a, b, c, d);

    return 0;
}
