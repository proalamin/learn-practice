/*
1. Input/Output Functions (from <stdio.h>)
printf(): Prints formatted output to the standard output (console).
scanf(): Reads formatted input from the standard input (keyboard).
gets(): Reads a line of text (deprecated, use fgets() instead).
fgets(): Reads a line of text including whitespace.
puts(): Writes a string to the console.
putchar(): Writes a single character to the console.
getchar(): Reads a single character from the console.


2. String Manipulation Functions (from <string.h>)
strlen(): Returns the length of a string.
strcpy(): Copies one string into another.
strncpy(): Copies the first n characters of a string into another.
strcat(): Concatenates (appends) one string to another.
strncat(): Appends the first n characters of one string to another.
strcmp(): Compares two strings (returns 0 if equal).
strncmp(): Compares the first n characters of two strings.
strchr(): Finds the first occurrence of a character in a string.
strstr(): Finds the first occurrence of a substring in a string.
strtok(): Tokenizes a string (splits a string into tokens).
memcpy(): Copies a block of memory.
memset(): Fills a block of memory with a specific value.


3. Mathematical Functions (from <math.h>)
sqrt(): Calculates the square root.
pow(): Raises a number to a power.
ceil(): Rounds up to the nearest integer.
floor(): Rounds down to the nearest integer.
fabs(): Returns the absolute value of a floating-point number.
abs(): Returns the absolute value of an integer (from <stdlib.h>).
sin(), cos(), tan(): Trigonometric functions (takes radians).
log(): Natural logarithm.
exp(): Exponential function.
round(): Rounds a floating-point number to the nearest integer.


4. Memory Management Functions (from <stdlib.h>)
malloc(): Allocates a block of memory.
calloc(): Allocates and initializes a block of memory.
realloc(): Resizes a previously allocated memory block.
free(): Frees a previously allocated memory block.


5. Utility Functions (from <stdlib.h> and <time.h>)
exit(): Terminates the program.
atoi(), atof(), atol(): Converts a string to an integer, float, or long integer.
rand(): Generates a random integer.
srand(): Seeds the random number generator.
time(): Returns the current time.


6. File Handling Functions (from <stdio.h>)
fopen(): Opens a file.
fclose(): Closes an open file.
fread(): Reads data from a file.
fwrite(): Writes data to a file.
fgets(): Reads a line from a file.
fprintf(), fscanf(): Formatted input/output for files.


7. Character Handling Functions (from <ctype.h>)
isalpha(): Checks if a character is alphabetic.
isdigit(): Checks if a character is a digit.
isalnum(): Checks if a character is alphanumeric.
isspace(): Checks if a character is a whitespace character.
toupper(), tolower(): Converts a character to upper or lower case.


8. Miscellaneous
sizeof(): Determines the size of a data type or variable.
assert() (from <assert.h>): Performs debugging checks during development.

*/

#include<stdio.h>
#include<math.h>

int main(){
    double a=10.511;

    printf("%lf\n", ceil(a));
    printf("%lf\n", floor(a));
    printf("%lf\n", round(a));

    printf("%lf\n", sqrt(25));

    printf("%lf\n", pow(2, 2));
}