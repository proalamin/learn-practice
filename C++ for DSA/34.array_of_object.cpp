#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    string name;
    int roll;
    int mark;
};

int main(){

    int n;
    cin>> n;
    cin.ignore();
    
    Student a[n];
    for(int i=0; i<n; i++){
        getline(cin, a[i].name);
        cin >> a[i].roll >> a[i].mark;
        cin.ignore();
    }

    for(int i=0; i<n; i++){
        cout <<a[i].name << " " <<a[i].roll << " " <<a[i].mark << endl;
    }

    return 0;
}