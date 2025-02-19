#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, e;
    cin >> n >> e;

    int adj_mat[n][e];

    // adj_mat all value 0 
    // for(int i=0; i<n; i++){
    //     for(int j=0; j<n; j++){
    //         adj_mat[i][j]=0;
    //     }
    // }

    // adj_mat all value 0 through function use
    memset(adj_mat, 0, sizeof(adj_mat));

    // diogonal set 1 value 
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++)
            if(i==j)
                adj_mat[i][j]=1;
        
    }

    while(e--){
        int a, b;
        cin >> a >> b;
        adj_mat[a][b] =1;
    }


    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << adj_mat[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}