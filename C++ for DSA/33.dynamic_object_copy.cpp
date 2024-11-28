/*
Question: Create a dynamic object named dhoni of the following class. Don’t use a constructor here, that means you need to fill the data by yourself.
Cricketer
{
	jersey_no;
	country;
}
Then make another dynamic object named kohli and copy the data of the dhoni object to kohli and after that delete the dhoni object. Then print the jersey_no and country of kohli object.
Note: At first try to do this, kohli=dhoni and see if it gives the correct output. If not, then think deeply why it didn’t work and try to copy the data manually like kohli->jersey_no=dhoni->jersey_no; 

*/

#include<bits/stdc++.h>
using namespace std;

class Cricketer{   
    public:
        int jersey_no;
        string country;
};

int main(){

    Cricketer *dhoni= new Cricketer;
    dhoni->jersey_no=107;
    dhoni->country="India";

    Cricketer *kholi= new Cricketer;
    *kholi=*dhoni; // copy through Assignment operator

    // manually copy
    // kholi->jersey_no=dhoni->jersey_no;
    // kholi->country=dhoni->country; 
    

    delete dhoni;

    cout<< kholi->jersey_no<< " "<< kholi->country;



    return 0;
}