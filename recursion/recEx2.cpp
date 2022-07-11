#include<iostream>
using namespace std;

int m, n;
int grid(int m, int n){
    if(m == 1 || n == 1)
    return 1;
    else return grid(m -1, n) + grid(m, n -1);
}

int main(){
    cout<<"Enter the dimensions: "<<endl;
    cin>>m>>n;
    cout<<grid(m, n);
    return 0;
}