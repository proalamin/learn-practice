#include<bits/stdc++.h>
using namespace std;

int main(){

    map<string, int> mp;
    int fre[100];
    fre[5] =20;
    mp["tamim"] = 2;            // logN
    mp["ramim"] = 5;
    mp["shamim"] = 50;
    mp["hamim"] = 0;


    cout << mp["ramim"] << endl;
    for(auto it = mp.begin(); it!= mp.end(); it++)      // O(NlogN)
    {
        cout << it->first << " "<< it->second << endl;  // logN
    }

    // value have or not
    if(mp.count("hamim"))
    {
        cout << "true";
    }
    else cout << "false";
    return 0;
}