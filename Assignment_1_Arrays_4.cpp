#include<bits/stdc++.h>
using namespace std;

void AddOne(vector<int>& digits)
{
	int index = digits.size() - 1;

	while (index >= 0 && digits[index] == 9)
		digits[index--] = 0;

	if (index < 0)
		digits.insert(digits.begin(), 1, 1);
	else
		digits[index]++;
}

int main()
{
	vector<int> digits{ 1, 2, 4 };

	AddOne(digits);

	for (int digit : digits)
		cout << digit << ' ';

	return 0;
}
