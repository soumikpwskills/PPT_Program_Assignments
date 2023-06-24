#include<bits/stdc++.h>
using namespace std;

void pushZerosToEnd(int arr[], int n)
{
	int count = 0;
	for (int i = 0; i < n; i++)
		if (arr[i] != 0)
			arr[count++] = arr[i];

	while (count < n)
		arr[count++] = 0;
}
int main()
{
	int arr[] = {0,1,0,3,12};
	int n = sizeof(arr) / sizeof(arr[0]);
	pushZerosToEnd(arr, n);
	printf("%s\n", "Array after pushing all zeros to end of array:");
	for (int i = 0; i < n; i++)
	printf("%d ", arr[i]);
	return 0;
}
