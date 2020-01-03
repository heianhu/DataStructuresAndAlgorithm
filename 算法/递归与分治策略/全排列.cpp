#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
using namespace std;

unsigned long long jiecheng(unsigned num)
{
	if (num == 1)
		return 1;
	else
		return num*jiecheng(num - 1);
}

// void Permutation(vector<unsigned long long> &per,int n, vector<unsigned long long> &lis, int k, int m)
// {
// 	//n++;
// 	if (k == m)
// 	{
// 		//n++;
// 		for (int i = 0; i <= m; i++)
// 		{
// 			per[n] = per[n] * 10 + lis[i];
// 		}
// 		//n++;
// 	}
// 	else
// 		for (int i=k;i<=m;i++)
// 		{
// 			swap(lis[k], lis[i]);
// 			Permutation(per, n, lis, k + 1, m);
// 			//n++;
// 			swap(lis[k], lis[i]);
// 			n++;
// 		}
// }

void Permutation(string &per, string &lis, int k, int m)
{
	//n++;
	if (k == m)
	{
		//n++;
		for (int i = 0; i <= m; i++)
			per += (lis[i]);
		per += '\n';
		//n++;
	}
	else
		for (int i = k; i <= m; i++)
		{
			swap(lis[k], lis[i]);
			Permutation(per, lis, k + 1, m);
			//n++;
			swap(lis[k], lis[i]);
			//n++;
		}
}

int main()
{
// 	vector<unsigned long long> lis{ 1,2,3 };
// 	unsigned long long num = jiecheng(lis.size());
// 	vector<unsigned long long> per(num);
// 	Permutation(per, 0, lis, 0, lis.size() - 1);
// 	for (auto a:per)
// 	{
// 		cout << a << endl;
// 	}
	string lis;
	cout << "请输入要全排列的数字或字母(无需空格分开)：";
	cin >> lis;
	cout << lis << "的全排列为：" << endl;
	string per;
	Permutation(per,lis, 0, lis.size() - 1);
	int b = 1;
	for (auto a : per)
	{
		cout << a;
// 		b++;
// 		if (b == lis.size())
// 		{
// 			cout << endl;
// 			b = 1;
// 		}
	}
    return 0;
}
