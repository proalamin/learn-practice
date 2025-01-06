/*
Queue Built-in Functions:
https://docs.google.com/document/d/1tiYAlnJZWbuamFGwLgR4tGm2TEm_FQe0hxF-rXy-9bU/edit?tab=t.0
*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    queue<int> q;

    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int val;
        cin >> val;
        q.push(val);
    }

    while(!q.empty()){
        cout << q.front() << " ";
        q.pop();
    }
    

    return 0;
}