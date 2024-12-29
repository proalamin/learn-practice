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

void insert_at_head(Node* &head, int val){
    Node* newNode= new Node(val);
    newNode->next=head;
    head = newNode;

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

    insert_at_head(head, 100);
    insert_at_head(head, 200);
    insert_at_head(head, 300);
    printLinkedList(head);
    

    return 0;
}