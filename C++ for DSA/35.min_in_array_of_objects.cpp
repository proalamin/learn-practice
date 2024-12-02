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
    cin >> n;
    Student a[n];

    for(int i=0; i<n; i++){
        cin >> a[i].name >> a[i].roll>>a[i].mark;
    }

    // int mn = INT_MAX;
    Student mn;
    mn.mark=INT_MAX;
    for(int i=0; i<n; i++){
        if(a[i].mark < mn.mark){
            mn= a[i];
        }
    }
    cout << mn.name << " " << mn.roll << " "<< mn.mark << endl;
    


    return 0;
}