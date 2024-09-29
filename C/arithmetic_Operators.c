/*
Arithmetic Operators in C

+ (addition),
- (subtraction), 
* (multiplication), 
/ (division), and 
% (modulus or modulo) note: remainder after division
*/

#include <stdio.h>

int main(){
    float num1, num2, addition, subtraction, multiplication, division;
    int num3, num4, modulo;  // % operator (modulus) cannot be used with floating-point numbers, as it only works with integers.

    num1=4;
    num2=3;
    num3=5;
    num4=3;


    addition= num1 + num2;
    subtraction= num1 - num2;
    multiplication= num1 * num2;
    division= num1 / num2;
    modulo= num3 % num4;

    printf("addition answer- %f\n", addition); 
    printf("subtraction answer- %f\n", subtraction); 
    printf("multiplication answer- %f\n", multiplication); 
    printf("division answer- %f\n", division); 
    printf("modulo answer- %d\n", modulo); 

    return 0;
}


