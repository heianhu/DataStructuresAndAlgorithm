#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int Partition(vector<long long> &a, int first, int last, long long x)
{
	int i = first - 1, j = last + 1;
	while (true)
	{
		while (a[++i] < x&&i < last);
		while (a[--j] > x);
		if (i >= j)
			break;
		swap(a[i], a[j]);
	}
	return j;
}

long long Select(vector<long long> &a, int first, int last, int k)
{
	//cout << "11111111" << endl;
	if (last - first < 75)
	{
		sort(a.begin() + first, a.begin() + last + 1);
		return a[first + k - 1];
	}
	//cout << "22222222" << endl;
	for (int i = 0; i <= (last - first - 4) / 5; ++i)
	{
		//cout << "333333" << endl;
		sort(a.begin() + (first + 5 * i), a.begin() + (first + 5 * i + 4) + 1);
		//cout << "4444444" << endl;
		swap(a[first + 5 * i + 2], a[first + i]);

	}
	//cout << "55555" << endl;
	long long x = Select(a, first, first + (last - first - 4) / 5, (last - first - 4) / 10);
	//cout << "6666666" << endl;
	int i = Partition(a, first, last, x),
		j = i - first + 1;
	//cout << "7777777" << endl;
	if (k <= i)
		return Select(a, first, i, k);
	else
		return Select(a, i + 1, last, k - j);
}

long long Random(long long x, long long y)
{
	return rand() % (y - x) + x;
}

int main()
{
	vector<long long>a;
	for (int i=0;i<10000;i++)
	{
		a.push_back(Random(0, 10000));
	}
	for (auto s : a)
	{
		cout << s << " ";
	}

	cout << endl << "最大的为:" << Select(a, 0, a.size() - 1, a.size()-4998) << endl;
	return 0;
}