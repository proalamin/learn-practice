#include<bits/stdc++.h>
using namespace std;

int main(){

    string s ="hello";
    // s.begin() -> pointer to the first element.
    // s.end() -> pointer to the next element after the last element of the string.
    cout << *s.begin()<<endl;
    cout << *(s.end()-1)<<endl;

    cout << endl;

    for(auto it = s.begin(); it<s.end(); it++){
        cout << *it << endl;
    }




    return 0;
}