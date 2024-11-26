#include<bits/stdc++.h>
using namespace std;

int main(){

    string s= "Hello";

    // 1
    string s1("Hello");

    // 2
    string s2("Hello", 3); // resize the string output->Hel

    //3
    string s3= "Hello World";
    string t(s3, 4); // n no char remove then print output-> o World


    //4
    string s4(5, 'A'); // output AAAAA


    cout << s4 << endl;


    return 0;
}