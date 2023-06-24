#include<bits/stdc++.h>
using namespace std;

int removeElement(int arr[], int n, int k)
{
    int count = 0;
	for (int i = 0; i < n; i++) {
		if (arr[i] != k)
			arr[count++] = arr[i];
	}

    for(int i=0;i<count;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return count;

}

int main()
{
    int nums[]={0,1,2,2,3,0,4,2};
    int val = 2;
    int n = sizeof(nums)/sizeof(nums[0]);
    cout<<removeElement(nums,n,val);
    return 0;

}