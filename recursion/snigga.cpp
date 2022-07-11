#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll extrema(ll arr[],ll i,ll n) 
{   
    if(i==n) 
    {   
        ll cnt=0;
        for(ll i=0;i<n;i++) 
        { 
            if(i+1<n && i-1>=0){
            if(arr[i]>arr[i-1] && arr[i]>arr[i+1]) 
             cnt++; 
            else if(arr[i]<arr[i-1] && arr[i]<arr[i+1]) 
             cnt++; 
            }   
        } 
        return cnt;   
    } 
    ll ans=0;
    arr[i]=0;
    ans+=extrema(arr,i+1,n);
    arr[i]=1; 
    ans+=extrema(arr,i+1,n); 
    arr[i]=2; 
    ans+=extrema(arr,i+1,n); 
    return ans;
}
// Driver Code
int main()//
{
   ll t; 
   cin>>t; 
   while(t--) 
   {   
     
     ll n; 
     cin>>n; 
     ll arr[n]; 
     cout<<extrema(arr,0,n)<<'\n';

   }
    return 0;
}