#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b;
    cin >> a >>b;
    
    // if(a<b){
    //     cout << a <<endl;
    // }else{
    //     cout << b << endl;
    // }
    cout << min(a,b)<<endl; // min function for find minimum value

    cout << max(a,b) << endl; // max function for maximum value

    swap(a,b);
    cout << a << " "<< b <<endl;


    return 0;
}