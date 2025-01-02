#include<bits/stdc++.h>
using namespace std;

int main(){
    
    list <int> l= {1,2,3,4,5,6,5};
    // l.remove(1);
    // l.sort();
    // l.sort(greater<int>());
    // l.unique(); // Deletes the duplicate values from the list. You must sort the list first.
    l.reverse();
    
    
    for(int val : l){
        cout << val << " ";
    }
    
    return 0;
}

/*
Operations functions-
https://docs.google.com/document/d/1IbS-qmFx6oRO-GyIG55yavdDUHpfHTNM/edit
 
*/