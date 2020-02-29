//https://www.hackerrank.com/challenges/preprocessor-solution/problem


/* Enter your macros here */
#define INF 1000000000
#define FUNCTION(a,b)
#define foreach(a, b) for(int i = 0; i < a.size(); i++)
#define io(a) cin >> a
#define minimum(a,b) a=a<b?a:b
#define maximum(a,b) a=a>b?a:b
#define toStr(a) #a


#include <iostream>
#include <vector>
using namespace std;

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif 

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
	return 0;

}
