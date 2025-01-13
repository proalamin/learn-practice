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

void inset_at_any_position(Node* head,int idx, int val){
    Node* newnode= new Node(val);
    Node* temp= head;
    for(int i=1; i<idx; i++){
        temp=temp->next;
    }
    newnode->next=temp->next;
    temp->next->prev=newnode;

    temp->next=newnode;
    newnode->prev=temp;
};

int main(){

    Node* head= new Node(10);
    Node* a= new Node(20);
    Node* tail= new Node(30);

    head->next=a;
    a->prev=head;

    a->next=tail;
    tail->prev=a;

    inset_at_any_position(head, 2, 100);
    
    print_forward(head);

    return 0;
}