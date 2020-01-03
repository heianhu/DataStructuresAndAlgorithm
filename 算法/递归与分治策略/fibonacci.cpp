#include "stdafx.h"
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

bool max(unsigned a, unsigned b)
{
	return a > b;
}

vector<int> f(vector<int> a, vector<int> b)
{
	bool which_big = max(a.size(), b.size());
	int num;
	if(which_big)
		num = a.size();
	else
		num = b.size();
	vector<int> ad(num + 1, 0);
	vector<int>::reverse_iterator pb = b.rbegin(),
		pa = a.rbegin();
	if (which_big)	//a大
	{
		while (pb!=b.rend())
		{
			ad[num] = *pb + *pa;
			num--;
			pb++;
			pa++;
		}
		while (pa!=a.rend())
		{
			ad[num] = *pa;
			num--;
			pa++;
		}

	}
	else	//b大
	{
		while (pa != a.rend())
		{
			ad[num] = *pb + *pa;
			num--;
			pb++;
			pa++;
		}
		while (pb != b.rend())
		{
			ad[num] = *pb;
			num--;
			pb++;
		}
	}
	int carry = 0;
	for (int i = ad.size() - 1; i >= 0; i--)
	{
		ad[i] += carry;
		carry = ad[i] / 10;
		ad[i] %= 10;
	}
	return ad;
}

vector<int> Fibonacci(vector<int> num)
{
	bool flag = 0;
	for (int i = 0; i < num.size(); i++)
	{
		auto a = num[i];
		if (a != 0 && i < num.size() - 1)
		{
			flag = 1;
			break;
		}
	}
	if ((!flag&&num[num.size() - 1] == 1)||(!flag&&num[num.size() - 1] == 2))
		return num = { 1 };
	else
	{
		vector<int> num_1(num);
		int i;
		for (i = num.size() - 1; i >= 0; i--)
		{
			auto a = num[i];
			if (a != 0)
				break;
		}
		num_1[i] -= 1;
		for (i += 1; i < num.size(); i++)
		{
			num_1[i] = 9;
		}
		vector<int> num_2(num_1);
		for (i = num_1.size() - 1; i >= 0; i--)
		{
			auto a = num_1[i];
			if (a != 0)
				break;
		}
		num_2[i] -= 1;
		for (i += 1; i < num_1.size(); i++)
		{
			num_2[i] = 9;
		}
		//cout << "1111" << endl;
		return f(Fibonacci(num_1),Fibonacci(num_2));
	}
}


int main()
{
	cout << "Please input the number to calculate:";
	vector<int> a;
	int temp, t;
	cin >> temp;
	t = temp;
	while (temp > 0)
	{
		a.push_back(temp % 10);
		temp /= 10;
	}
	reverse(a.begin(), a.end());
	//非递归实现
	cout << "非递归实现，速度较快" << endl;
	bool flag = 0;
	vector<int> a1{ 0 }, a2 = { 1 }, num = { 1 };
	for (int i=1;i<t;i++)
	{
		num = f(a1 , a2);
		a1 = a2;
		a2 = num;
	}
	for (auto s : num)
	{
		if (s != 0||num.size()==1)
			flag = 1;
		if (!flag)
			continue;
		cout << s;
	}
	cout << endl;
	//递归实现
	cout << "递归实现，速度较慢" << endl;
	flag = 0;
	for (auto s : Fibonacci(a))
	{
		if (s != 0)
			flag = 1;
		if (!flag)
			continue;
		cout << s;
	}
	cout << endl;
    return 0;
}

