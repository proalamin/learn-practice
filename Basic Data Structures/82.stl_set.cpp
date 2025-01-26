#include<bits/stdc++.h>
using namespace std;

int main(){

    set<int> s;
    int n;
    cin >> n;
    while(n--)
    {
        int val;
        cin >> val;
        s.insert(val);  // logN
    }

    for(auto it =s.begin(); it!= s.end(); it++)
    {
        cout << *it << endl;
    }


    // any value have or not
    if(s.count(4)) cout << "true"; // logN
    else cout << "false";

    return 0;
}