#include<bits/stdc++.h>
using namespace std;

int main(){
    
    list <int> l= {1,2,3,4,5,6,5};
    
    cout << l.back() <<endl;
    cout << l.front() << endl;
    
    cout << *next(l.begin(), 2) << endl;
    
    cout << *l.begin() << endl;
    

    return 0;
}

/*
Iterators-
https://docs.google.com/document/d/1IbS-qmFx6oRO-GyIG55yavdDUHpfHTNM/edit
 
*/