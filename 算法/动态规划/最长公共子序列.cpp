// EXPERIMENT1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void LCSLength(string &x, string &y, vector<vector<int>> &c)
//二维数组c记录Xi,Yj的的最长公共子序列的长度
{
	int i, j, m = x.length(), n = y.length();
	for (i = 1; i <= m; i++)
		for (j = 1; j <= n; j++)
			if (x[i-1] == y[j-1])
				c[i][j] = c[i - 1][j - 1] + 1;
			else if (c[i - 1][j] >= c[i][j - 1])
				c[i][j] = c[i - 1][j];
			else
				c[i][j] = c[i][j - 1];
}

void LCS(int i, int j, string &x, vector<vector<int>> &c)
//当c[i][j] == c[i-1][j]时，表示X[i],Y[j]的最长公共子序列与X[i-1],Y[j]的最长公共子序列相同(数组往上移动)
//当c[i][j] == c[i][j-1]时，X[i],Y[j]的最长公共子序列与X[i],Y[j-1]的最长公共子序列相同(数组往左移动)
//当上两个均不满足时，表示X[i],Y[j]的最长公共子序列由X[i-1],Y[j-1]的最长公共子序列在尾部加上Xi所得到的子序列(数组往左上移动)
{
	if (i == 0 || j == 0)
		return;
	if (c[i][j] == c[i - 1][j])
		LCS(i - 1, j, x, c);
	else if(c[i][j] == c[i][j - 1])
		LCS(i, j - 1, x, c);
	else
	{
		LCS(i - 1, j - 1, x, c);
		cout << x[i-1];
	}
}

int main()
{
d1:	int ccc;
	string x, y;
	cout << "选择:" << endl
		<< "1.x={ABCBDAB}, y={BDCABA}" << endl
		<< "2.x={zhejiang university of technology}, y={zhejiang university city college}" << endl;
	cin >> ccc;
	if (ccc == 1)
	{
		x = "ABCBDAB";
		y = "BDCABA";
	}
	else if (ccc == 2)
	{
		x = "zhejiang university of technology";
		y = "zhejiang university city college";
	}
	else
	{
		system("cls");
		goto d1;
	}
	vector<vector<int>> c;
	vector<int> temp;
	for (int j = 0; j <= y.length(); j++)
		temp.push_back(0);
	for (int i = 0; i <= x.length(); i++)
		c.push_back(temp);
	LCSLength(x, y, c);
	LCS(x.length(), y.length(), x, c);
	cout << endl;
	return 0;
}

