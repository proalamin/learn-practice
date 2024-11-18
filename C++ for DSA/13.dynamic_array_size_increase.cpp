#include"bits/stdc++.h"
using namespace std;

int main(){
    int *x = new int[3];
     for(int i=0; i<3; i++){
        cin >> x[i];
    }

    int *b= new int[5];
    for(int i=0; i<3; i++){
        b[i]=x[i];
    }
    b[3]=40;
    b[4]=50;
    delete[] x; // dynamic array delete

    for(int i=0; i<5; i++){
        cout << b[i] << " ";
    }

    return 0;
}