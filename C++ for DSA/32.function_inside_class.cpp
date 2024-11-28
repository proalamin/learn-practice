#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    string name;
    int roll;
    Student(string name, int roll){
        this->name=name;
        this->roll=roll;
    }
    void hello(){
        cout << "Hello from "<< name << endl; 
    }
};

int main(){

    Student sakib("Sakib", 23);
    Student rakib("Rakib", 25);
    // cout << sakib.name <<endl;
    sakib.hello();
    rakib.hello();


    return 0;
}