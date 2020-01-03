#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

int binary(vector<int> bin,int key)
{
	int left = 0, right = bin.size() - 1;
	while (left <= right)
	{
		int  mid = (left + right) / 2;
		if (bin[mid] == key)
			return mid;
		else if (bin[mid] < key) 
			left = mid + 1;
		else
			right = mid - 1;
	}
	return -1;
}
int main()
{
	cout << "请输入要查找的序列元素个数:";
	int n;
	cin >> n;
	vector<int> bin(n);
	cout << "请输入序列的元素:" << endl;
	for (auto &a:bin)
		cin >> a;
	cout << "请输入要找的元素:";
	int key;
	cin >> key;
	int num = binary(bin,key);
	if (num == -1)
		cout << key << "不在该序列中" << endl;
	else
		cout << key << "在该序列中的第" << num + 1 << "位" << endl;
    return 0;
}

