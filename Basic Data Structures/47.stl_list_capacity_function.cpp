/*
Capacity-
	
Name                Details                                             Time Complexity
myList.size()       Returns the size of the list.                       O(1)
myList.max_size()   Returns the maximum size that the list can hold.    O(1)
myList.clear()      Clears the list elements.                           O(N)
myList.empty()      Return true/false if the list is empty or not.      O(1)
myList.resize()     Change the size of the list.                        O(K); where K is the difference between new size and current size.

*/

#include<bits/stdc++.h>
using namespace std;

int main(){

    list<int> l(10,3);
    
    // l.clear();
    // l.resize(1);
    for( int val : l){
        cout << val << endl;
    }

    return 0;
}
