//https://www.hackerrank.com/challenges/vector-erase/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, temp;
    vector<int> v;
    cin>>N;
    // fill vector
    for(int i=0;i<N;i++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    //remove itemp specified in 3rd line
    cin>>temp;
    if(temp<v.size())
        v.erase(v.begin()+temp-1);
    
    //remove range specified in 4th line
    int a,b;
    cin>>a>>b;

    if(a<b && b<v.size())
        v.erase(v.begin() +a-1, v.begin()+b-1);
    
    //print out remaining vector elements
    cout<<v.size()<<endl;

    /*
    It's a newer structure called a range-based for-loop (C++11). It takes anything that can be iterated through (in this case v), and goes through each item one-at-a-time, placing the value into "auto (underscore)v". Auto is a newer type (since C++11), that automatically determines what is being passed to it. So it basically detects that this is an int. It comes in handy when you have complicated types, like iterators of maps and such. It's basically equivalent to:
    
    for(int i; i<v.size(); i++) 
    {
        int j=v[i];
    }
    
    */
    for(auto _v : v)
        cout<<_v<<" ";
    cout<<endl;

    return 0;
}

