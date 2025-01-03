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
}


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

void reverse_doubly(Node* head, Node* tail){
    
    for(Node *i=head, *j=tail; i!=j && i->prev!=j; i=i->next, j=j->prev){
        swap(i->val, j->val);
    }
 
}

int main(){

    Node* head= NULL;
    Node* tail= NULL;

    int val;
    while(1){
        cin >> val;
        if(val == -1){
            break;
        }
        insert_at_tail(head, tail, val);
    }

    print_forward(head);
    reverse_doubly(head, tail);
    print_forward(head);

    return 0;
}