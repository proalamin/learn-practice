#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    string name;
    int roll;
    int mark;
};

bool cmp(Student l, Student r)
{

    /* sort mark lowest to higestr */
    // if(l.mark < r.mark){
    //     return true;
    // }else{
    //     return false;
    // }


    /* highest mark to lowest mark then if any mark is equal then sort lowest roll to highest roll */
    if(l.mark > r.mark){
        return true;
    }
    else if(l.mark < r.mark){
        return false;   
    }
    else if(l.mark == r.mark){
        if(l.roll < r.roll){
            return true;
        }
        else{
            return false;
        }
        
        /*or same line 29-34*/
        // return l.roll < r.roll;
    }
}

int main(){
    int n;
    cin >> n;
    Student a[n];

    for(int i=0; i<n; i++){
        cin >> a[i].name >> a[i].roll>>a[i].mark;
    }

    sort(a, a+n, cmp);
    for(int i=0; i<n; i++){
        cout << a[i].name<< " " << a[i].roll <<" " << a[i].mark << endl;
    }
    

    return 0;
}