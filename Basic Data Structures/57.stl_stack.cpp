#include<bits/stdc++.h>
using namespace std;

int main(){

    stack<int> st;
    
    int n;
    cin >> n;
    for(int i=0; i <n; i++){
        int val;
        cin >> val;
        st.push(val);
    }

    // if(!st.empty()){
    //     cout << st.top() << endl;
    // }

    // if(!st.empty()){
    //     st.pop();
    // }

    while(!st.empty()){
        cout << st.top() << " ";
        st.pop();
    }


    return 0;
}