/*
Vector Built-in Functions:
https://docs.google.com/document/d/1nxpbS-5RKFSwcJ6mHv3P2Vru9HTqXOeB/edit
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);

    cout << v.size() << endl;
    // v.clear();
    
    // v.resize(2);
    v.resize(5, 100);
    cout << v.size() << endl;
    for(int i=0; i<v.size(); i++){
        cout << v[i] << " ";
    }


    // cout << v[2] << endl;




    return 0;
}