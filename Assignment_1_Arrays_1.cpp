#include <bits/stdc++.h>
 
using namespace std;

bool findPair(int A[], int size, int x)
{
    for (int i = 0; i < (size - 1); i++) {
        for (int j = (i + 1); j < size; j++) {
            if (A[i] + A[j] == x) {
                cout<<"Indices are : "<<i<<","<<j<<endl;
            }
        }
    }
 
    return 0;
}
 
int main()
{
    int A[] = {2,7,11,15};
    int x = 9;
    int size = sizeof(A) / sizeof(A[0]);
 
   findPair(A,size,x);
 
    return 0;
}