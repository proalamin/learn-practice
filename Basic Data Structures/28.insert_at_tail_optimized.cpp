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

void insert_at_tail(Node* &head, Node* &tail, int val){
    Node* newNode= new Node(val);

    //Corner case-> if linked list is empty
    if(head== NULL){
        head =newNode;
        tail = newNode;
        return;
    }

    // Node* temp=head;
    // while(temp->next != NULL){
    //     temp= temp->next;
    // }

    // complexity is now O(1)
    tail->next= newNode;
    tail = tail->next;

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
    Node* tail= new Node(30);

    head->next=a;
    a->next=tail;

    insert_at_tail(head, tail, 40);
    insert_at_tail(head, tail, 50);
    insert_at_tail(head, tail, 530);
    printLinkedList(head);

    cout << "tail- " << tail->val;
    

    return 0;
}