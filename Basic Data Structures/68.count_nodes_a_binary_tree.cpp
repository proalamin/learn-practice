#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
        int val;
        Node* left;
        Node* right;
    Node(int val){
        this->val = val;
        this->left = NULL;
        this->right = NULL;

    }
};

Node* input_tree(){
    int val;
    cin >> val;
    Node* root;
    if(val == -1) root = NULL;
    else root = new Node(val);
    queue<Node *>q;
    if(root) q.push(root);
    while(!q.empty())
    {
        Node* p =q.front();
        q.pop();

        int l,r;
        cin >> l >> r;
        Node *myLeft, *myRight;
        if(l == -1) myLeft = NULL;
        else myLeft = new Node(l);
        if(r == -1) myRight = NULL;
        else myRight = new Node(r);

        // node connection
        p->left = myLeft;
        p->right = myRight;

        // children push
        if(p->left)
            q.push(p->left);
        if(p->right)
            q.push(p->right);

    }
    return root;
}


int count_nodes(Node* root)
{
    if(root == NULL)
        return 0;
    int l = count_nodes(root->left);    
    int r = count_nodes(root->right);

    return l+r+1;   
}

int main(){
    Node* root = input_tree();
    cout << count_nodes(root);

    return 0;
}