/*
Vector Built-in Functions:
https://docs.google.com/document/d/1nxpbS-5RKFSwcJ6mHv3P2Vru9HTqXOeB/edit
*/


#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> v={1,2,3,4};

    // v.insert(v.begin()+2, 100);

    // vector<int> v2={100,200,300};
    // v.insert(v.begin()+2, v2.begin(), v2.end());

    // v.erase(v.begin()+2);
    // v.erase(v.begin()+1, v.end()-1);

    // replace(v.begin(), v.end(),2,100);

    auto it =find(v.begin(), v.end(), 100);
    if(it==v.end()){
        cout << "not end";
    }else{
        cout << "found";
    }

    for(int x : v){
        cout << x << " ";
    }


    return 0;
}