#include<bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin>>n;
    // int a[n];
    // vector<int>v(n); //if size declare input like for loop input

    vector<int>v; // if no give size then use push back
    for(int i=0; i<n; i++){
        // cin >> v[i]; // when size declare work this
        
        int x;
        cin >> x;
        v.push_back(x);
    }
    for(int i=0; i<n; i++){
        cout << v[i] << " ";
    }



    return 0;
}