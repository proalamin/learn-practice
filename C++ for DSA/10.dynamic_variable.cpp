#include<bits/stdc++.h>
using namespace std;

int main(){

    int x=10;

    int *p= new int;
    *p=11;
    delete p; // if want to delete dynamic variable use "delete" keyword
    cout << *p << endl;

    return 0;
}