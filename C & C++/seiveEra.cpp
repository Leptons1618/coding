// #include<bits/stdc++>
#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

void sieve(int n){
    bool prime[n+1];
    memset(prime, true, sizeof(prime));

    for(int i = 2; i*i<=n; i++){
        if(prime[i]==true){
            for(int j = i*i; j <= n; j += i)
            prime[j] = false;
        }
    }
    for(int p = 2; p <= n; p++)
        if(prime[p])
            cout<<p<<" ";
}

int main(){
    sieve(100);
    return 0;
}

