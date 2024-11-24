#include<bits/stdc++.h>
using namespace std;

int main(){

    // s.size() -> returns the size of the string.
    string s= "hello string...";
    cout << s.size() << endl;

    // s.max_size() -> returns the maximum size that string can hold.   // 10^6
    cout << s.max_size() << endl;

    //s.capacity() -> returns current available capacity of the string.
    cout << s.capacity() << endl;

    //s.clear() -> clear the string.
    // s.clear();
    cout << s << endl;

    //s.empty() -> return true/false if the string is empty.
    if(s.empty()==true){
        cout << "empty"<< endl;
    }else{
        cout << "not empty"<< endl;

    }

    //s.resize() -> change the size of the string.
    s.resize(15); // re-size 
    s.resize(20, 'x'); // if size is big more then string componenet then the extra size print x or what ever we give.
    cout << s << endl;


    return 0;
}