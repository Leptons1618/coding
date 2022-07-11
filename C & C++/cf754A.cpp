// #include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    while(n--)
    {
        int a, b, c;
        cin>>a>>b>>c;
        (abs(a+b-(2*c))%3==0)?cout<<0<<"\n":cout<<1<<"\n";
    }
    return 0;
}