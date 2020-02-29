//https://www.hackerrank.com/challenges/c-tutorial-pointer/problem

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int x=*a;    
    *a = *a + *b;
    if (*b > x)
    { 
        *b =  (*b - x) ;
     }
     else
     {
         *b = (x - *b);
     }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}


