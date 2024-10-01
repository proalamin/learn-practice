/*
Relational Operators:

Operator	Meaning of Operator	        Example
==	        Equal to	                5 == 3 is evaluated to 0
>	        Greater than	            5 > 3 is evaluated to 1
<	        Less than	                5 < 3 is evaluated to 0
!=	        Not equal to	            5 != 3 is evaluated to 1
>=	        Greater than or equal to	5 >= 3 is evaluated to 1
<=	        Less than or equal to	    5 <= 3 is evaluated to 0

*/

#include <stdio.h>
int main()
{
    int a = 5, b = 5, c = 10;

    printf("%d == %d is %d \n", a, b, a == b);
    printf("%d == %d is %d \n", a, c, a == c);
    printf("%d > %d is %d \n", a, b, a > b);
    printf("%d > %d is %d \n", a, c, a > c);
    printf("%d < %d is %d \n", a, b, a < b);
    printf("%d < %d is %d \n", a, c, a < c);
    printf("%d != %d is %d \n", a, b, a != b);
    printf("%d != %d is %d \n", a, c, a != c);
    printf("%d >= %d is %d \n", a, b, a >= b);
    printf("%d >= %d is %d \n", a, c, a >= c);
    printf("%d <= %d is %d \n", a, b, a <= b);
    printf("%d <= %d is %d \n", a, c, a <= c);

    return 0;
}