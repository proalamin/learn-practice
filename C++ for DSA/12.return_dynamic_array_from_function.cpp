#include<bits/stdc++.h>
using namespace std;

int* fun(){
    // int a[5]; // if use static array got a waring or segmentation fault bcz want to return array and static array after return function delete value or address
    
    int *a = new int[5];
    for(int i=0; i<5; i++){
        cin >> a[i];
    }
    return a;
}


int main(){
    int* x=fun();

    for(int i=0; i<5; i++){
        cout << x[i] << " ";
    }

    return 0;
}