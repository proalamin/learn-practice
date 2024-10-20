/*
Escape Sequence     Meaning
\a                  Alarm or Beep
\b                  Backspace
\f                  Form Feed
\n                  New Line
\r                  Carriage Return
\t                  Tab (Horizontal)
\v                  Vertical Tab
\\                  Backslash
\'                  Single Quote
\"                  Double Quote
\?                  Question Mark
\nnn                octal number
\xhh                hexadecimal number
\0                  Null

*/

#include<stdio.h>

int main(){

    char escape[]="Bangladesh is a \"beautiful\" country";
    fputs(escape, stdout);

    return 0;
}