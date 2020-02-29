//https://www.hackerrank.com/challenges/cpp-sets/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int iCount;
    set<int> ss;
    cin>>iCount;
    for(int i=0;i<iCount;i++)
    {
        int type,query;
        cin>>type>>query;
        switch(type)
        {
            case 1: ss.insert(query);break;
            case 2: ss.erase(query);break;
            case 3: cout<<(ss.find(query)==ss.end()?"No":"Yes")<<endl;break;
        }
    }
    return 0;
}



