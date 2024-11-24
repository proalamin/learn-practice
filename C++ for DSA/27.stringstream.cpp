#include<bits/stdc++.h>
using namespace std;

int main(){

    string s;
    getline(cin, s);
    cout << s << endl;
    stringstream ss(s);
    int cnt=0;
    string word;
    while(ss>>word){
        cout << word << endl;
        cnt++;
    }
    cout << cnt <<endl;
    

    return 0;
}