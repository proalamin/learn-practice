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
    tail->next= newNode;
    tail = newNode;

}

void printLinkedList(Node* head){
    Node* temp=head;
    while(temp != NULL){
        cout << temp->val << endl;
        temp= temp->next;
    }
}

void sort_link_list(Node* head){
    for(Node* i= head; i->next !=NULL; i=i->next){
        for(Node* j= i->next; j !=NULL; j=j->next){

            // ascending order
            if(i->val > j->val){
                swap(i->val, j->val);
            }

            // descending order - just condition change
            // if(i->val < j->val){
            //     swap(i->val, j->val);
            // }
        }
    }
}


int main(){
    
    Node* head = NULL;
    Node* tail = NULL;

    int val;
    while(1){
        cin >> val;
        if(val == -1){
            break;
        }
        insert_at_tail(head, tail, val);
    }

    sort_link_list(head);

    printLinkedList(head);
    

    return 0;
}