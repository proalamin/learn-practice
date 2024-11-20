#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    int roll;
    int cls;
    double gpa;

    // if we want constructor function variable name same then use this or arrow sign
    Student(int roll, int cls, double gpa){
        (*this).roll =roll;
        // this->roll=roll;
        
        (*this).cls=cls;
        (*this).gpa=gpa;
    }
};

int main(){

    Student rahim(34,5,3.44);

    Student karim(4,5,5);

    cout << rahim.roll << " " << rahim.cls << " " << rahim.gpa << endl;
    cout << karim.roll << " " << karim.cls << " " << karim.gpa << endl;


    return 0;
}