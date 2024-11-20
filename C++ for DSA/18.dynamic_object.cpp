#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    int roll;
    int cls;
    double gpa;

    Student(int r, int c, double g){
        roll =r;
        cls=c;
        gpa=g;
    }
};

int main(){

    Student rahim(34,5,3.44);

    Student* karim= new Student(4,5,5);

    cout << rahim.roll << " " << rahim.cls << " " << rahim.gpa << endl;
    cout << karim->roll<< " " << karim->cls << " " << karim->gpa << endl;


    return 0;
}