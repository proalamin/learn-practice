    #include<bits/stdc++.h>
    using namespace std;

    int main(){

        list<int> l={10,20,30,3,4,41};
        list<int> l2={40,50,60};

        // list<int> l2;
        // l2=l;
        // l2.assign(l.begin(), l.end());
        // l.push_back(40);
        // l.push_front(100);

        // l.pop_back();
        // l.pop_front();

        // cout << *next(l.begin(), 2);
        
        // l.insert(next(l.begin(),2), l2.begin(), l2.end());
        
        // l.erase(next(l.begin(), 3));
        // l.erase(next(l.begin(), 3), next(l.begin(), 5));
        
        // replace(l.begin(), l.end(),3, 300);
        
        auto it=find(l.begin(), l.end(), 3);
        if(it == l.end()){
            cout << "not found" << endl;
        }else{
             cout << "found" << endl;
        }
        

        for(int val : l){
            cout << val << " ";
        }


        return 0;
    }

/*
Modifiers-
https://docs.google.com/document/d/1IbS-qmFx6oRO-GyIG55yavdDUHpfHTNM/edit
*/