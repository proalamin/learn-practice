#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
        int val;
        Node* next;
    Node(int val){
        this->val = val;
        this->next = NULL;
    }
};

void insert_at_any_position(Node* &head,int idx, int val){
    Node* newNode= new Node(val);
    Node* temp=head;
    for(int i=0; i<idx-1; i++){
        temp= temp->next;
    }
    newNode->next= temp->next;
    temp->next=newNode;


}

void printLinkedList(Node* head){
    Node* temp=head;
    while(temp != NULL){
        cout << temp->val << endl;
        temp= temp->next;
    }
}

int main(){

    Node* head= new Node(10);
    Node* a= new Node(20);
    Node* b= new Node(30);

    head->next=a;
    a->next=b;

    insert_at_any_position(head, 2, 100);
    printLinkedList(head);

    return 0;
}