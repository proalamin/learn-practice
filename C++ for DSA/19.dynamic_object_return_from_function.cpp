#include<bits/stdc++.h>
using namespace std;

class Student{
    public:
    int roll;
    int cls;
    double gpa;

    Student(int roll, int cls, double gpa){
        (*this).roll =roll;
        // this->roll=roll;
        
        (*this).cls=cls;
        (*this).gpa=gpa;
    }
};

Student* fun(){
    Student* rahim= new Student(34,5,3.44);
    // Student* p= &rahim;
    return rahim;

}


int main(){

    Student* obj=fun();
    
    cout << obj->roll<< " " << obj->cls << " " << obj->gpa << endl;


    return 0;
}