/*
List Built-in Functions: 
https://docs.google.com/document/d/1IbS-qmFx6oRO-GyIG55yavdDUHpfHTNM/edit
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    list<int> l(10,3);
    
    for( int val : l){
        cout << val << endl;
    }

    return 0;
}

