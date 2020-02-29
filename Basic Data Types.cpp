//https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int inta;
    long longa;
    char chara;
    float floata;
    double doublea;
    cin >>inta>>longa>>chara>>floata>>doublea;
    cout<<inta<<endl<<longa<<endl<<chara<<endl;
    cout.precision(3);
    cout<<fixed<<floata<<endl;
    cout.precision(9);
    cout<<fixed<<doublea<<endl;
    return 0;
}


