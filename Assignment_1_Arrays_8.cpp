#include <bits/stdc++.h>
using namespace std;

int findRepeating(int arr[], int N)
{
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (arr[i] == arr[j])
				return arr[i];
		}
	}
}

int main()
{
	int arr[] = {1,2,2,4};
	int N = sizeof(arr) / sizeof(arr[0]);

    int f = findRepeating(arr,N);

	cout << f<<" "<<f+1<<endl;
	return 0;
}
