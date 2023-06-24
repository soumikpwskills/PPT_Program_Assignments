// C++ program to Check if a given array contains duplicate
// elements within k distance from each other
#include <bits/stdc++.h>
using namespace std;

bool checkDuplicates(int arr[], int n, int k)
{
	for (int i = 0; i < n; i++) {
		int j = i + 1;
		while (j < n) {
			if (arr[i] == arr[j])
				return true;
			j++;
		}
	}
	return false;
}

int main()
{
	int arr[] = { 1, 2, 3, 1 };
	int n = sizeof(arr) / sizeof(arr[0]);
	if (checkDuplicates(arr, n, 3))
		cout << "true";
	else
		cout << "false";
}

