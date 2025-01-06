#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
        int val;
        Node* next;
        Node* pre;
    Node(int val){
        this->val = val;
        this->next = NULL;
        this->pre= NULL;
    }
};

class myQueue{
    public:
        Node* head = NULL;
        Node* tail = NULL;
        int sz=0;

        void push(int val){
            sz++;
            Node* newNode= new Node(val);
            if(head == NULL){
                head = newNode;
                tail= newNode;
                return;
            }
            tail->next= newNode;
            newNode->pre=tail;
            tail= newNode;
        }

        void pop(){
            sz--;
            Node* deleteNode= head;
            head = head->next;
            delete deleteNode;
            if(head == NULL){
                tail = NULL;
                return;
            }
            head->pre=NULL;
        }

        int front(){
            return head->val;
        }

        int back(){
            return tail->val;
        }

        int size(){
            return sz;
        }

        bool empty(){
            if(head== NULL){
                return true;
            }else{
                return false;
            }
        }
};


int main(){

    myQueue q;
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        int val;
        cin >> val;
        q.push(val);
    }

    while(!q.empty()){
        cout << q.front() << " ";
        q.pop();
    }

    return 0;
}