#include<bits/stdc++.h>
using namespace std;

int main(){

    // s+= -> append another string.
    string s= "Hello I am";
    string s2= "String...";
    s +=s2;
    // string s3 =s+s2;
    cout << s << endl;

    //s+= -> append another string.
    s.append(s2);
    cout << s << endl;


    //s.push_back() -> add character to the last of the string.
    s.push_back('t');
    // s += 'b'; // others method add character of the last of the string
    cout << s << endl;

    // s.pop_back() -> remove the last character of the string.
    s.pop_back();
    cout << s << endl;

    // s.assign() -> assign string.
    string s3="okk";
    // s.assign(s3);
    cout << s << endl;

    //s.erase() -> erase characters from the string.
    // s.erase(5);
    // s.erase(2,2); // index to char delete 
    cout << s << endl;

    //s.replace() -> replace a portion of the string.
    // s.replace(index, how much char delete, new string);
    s.replace(5, 2, " BD");
    cout << s << endl;

    //s.insert() -> insert a portion to a specific position.
    s.insert(6, "BB");
    cout << s << endl;



    return 0;
}