/*
Conditional Statements:

*/

#include <stdio.h>
int main() {
    int number=5;

    // true if number is less than 0
    if (number < 0) {
        printf("You entered %d.\n", number);
    }
    printf("The if statement is easy.\n");


    // if else
    if  (number%2 == 0) {
        printf("%d is an even integer.\n",number);
    }
    else {
        printf("%d is an odd integer.\n",number);
    }

    // if else if else
    int number1, number2;
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    //checks if the two integers are equal.
    if(number1 == number2) {
        printf("Result: %d = %d\n",number1,number2);
    }

    //checks if number1 is greater than number2.
    else if (number1 > number2) {
        printf("Result: %d > %d\n", number1, number2);
    }

    //checks if both test expressions are false
    else {
        printf("Result: %d < %d\n",number1, number2);
    }

    // nested if else
    if (number1 >= number2) {
      if (number1 == number2) {
        printf("Result: %d = %d\n",number1,number2);
      }
      else {
        printf("Result: %d > %d\n", number1, number2);
      }
    }
    else {
        printf("Result: %d < %d\n",number1, number2);
    }

    return 0;
}
