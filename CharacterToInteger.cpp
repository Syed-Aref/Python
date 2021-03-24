#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;

#define mpr make_pair
#define pbk push_back
#define psh push
#define fir first
#define sec second
#define ln "\n"


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    /**
    97->a , 98->b , ... , 122->z
    65->A , 66->B , ... , 90->Z
    48->0 , 49->1 , ... , 57->10
    **/
    cout << 'a' - 'a' + 1 << endl; // 1
    cout << 'a' - 97 + 1 << endl; // 1

    cout << '0' - '0' << endl; // 0
    cout << '1' - '0' << endl; // 1
    cout << '0' - 48 << endl; // 0
    cout << '1' - 48 << endl; // 0
    
    return 0;
}
