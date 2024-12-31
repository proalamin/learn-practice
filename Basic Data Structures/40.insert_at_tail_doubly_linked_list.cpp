#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
        int val;
        Node* next;
        Node* prev;
    Node(int val){
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

void print_forward(Node* head){
    Node* temp= head;
    while(temp != NULL){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
};


void insert_at_tail(Node* &head, Node* &tail, int val){
    Node* newnode= new Node(val);

    // if head or tail is NULL
    if(head == NULL){
        head=newnode;
        tail=newnode;
        return;
    }
    tail->next=newnode;
    newnode->prev=tail;
    tail= newnode;
}

int main(){

    Node* head= NULL;
    // Node* head= new Node(10);
    // Node* a= new Node(20);
    // Node* tail= new Node(30);
    Node* tail= NULL;

    // head->next=a;
    // a->prev=head;

    // a->next=tail;
    // tail->prev=a;


    insert_at_tail(head, tail, 55);
    insert_at_tail(head, tail, 555);
    print_forward(head);

    return 0;
}