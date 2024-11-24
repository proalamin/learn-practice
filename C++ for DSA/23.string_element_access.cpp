#include<bits/stdc++.h>
using namespace std;

int main(){

    string s;
    cin >> s;

    //s[i] -> access the i th index of the string.
    cout << s[0]<< endl;

    //s.at(i) -> access the i th index of the string.
    cout << s.at(0) << endl;

    //s.back() -> access the last element of the string.
    cout << s.back() << endl;

    //s.front() -> access the first element of the string.
    cout << s.front() << endl;

    return 0;
}