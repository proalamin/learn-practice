


#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin >> n;
    
    // if any loop increment * or dicrement / this is 0Logn
    for(int i=1; i<=n; i*=2){
        cout << i << endl;
    }


    return 0;
}