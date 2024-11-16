#include<iostream>
using namespace std;


int main(){

    int x;
    char c;
    double d;

    cin >> x >> c >> d;
    cout << x <<" "<< c << " " << d <<endl;

    char name='c';
    int asci=name;
    // cout << asci << endl;
    cout << (int)name << endl; // output asci value bcz there type casting

    return 0;
}