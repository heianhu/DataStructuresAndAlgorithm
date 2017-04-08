#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

double MaxSum_first(const vector<double> &a)
{
	double sum = 0, b = 0;
	for (int i = 0; i < a.size(); ++i)
	{
		if (b > 0)
			b += a[i];
		else
			b = a[i];
		if (b > sum)
			sum = b;
	}
	return sum;
}

void readfile(vector<int> &year, vector<double> &heizishu)
{
	ifstream in("..\\太阳黑子.txt");
	int y;
	double h;
	while (!in.eof())
	{
		in >> y >> h;
		year.push_back(y);
		heizishu.push_back(h);
	}
	for (int i= heizishu.size()-1;i>0;)
	{
		heizishu[i] -= heizishu[--i];
	}
}

double MaxSum_second(const vector<int>year, const vector<double> &a, vector<int> &in_year)
{
	double sum = 0, b = 0;
	vector<int> temp_year;
	for (int i = 0; i < a.size(); ++i)
	{
		if (a[i] > 0)
		{
			b += a[i];
			temp_year.push_back(year[i]);
		}
		else
		{
			b = 0;
			temp_year.clear();
			temp_year.push_back(year[i]);
		}
		if (b > sum)
		{
			sum = b;
			in_year = temp_year;
		}
	}
	return sum;
}

int main()
{
d1:	int ccc;
	cout << "选择:" << endl
		<< "1.做(-2,11,-4,13,-5,-2)的最大子段和问题" << endl
		<< "2.做太阳黑子问题" << endl;
	cin >> ccc;
	if (ccc == 1)
	{
		vector<double> test1{ -2,11,-4,13,-5,-2 };
		double sum = MaxSum_first(test1);
		cout <<"(-2,11,-4,13,-5,-2)的最大子段和为:"<< sum << endl;
	}
	else if (ccc == 2)
	{
		vector<int> year, in_year;
		vector<double> heizishu;
		readfile(year, heizishu);
//		cout << year.size() << endl
//			<< heizishu.size() << endl;
		double sum = MaxSum_second(year, heizishu, in_year);
//		cout << sum << endl;
 		cout << "在"<<
			in_year[0]<<"--"<<in_year[in_year.size()-1]<<
			"这几年间太阳黑子迎来了最大爆发" << endl;
	}
	else
	{
		system("cls");
		goto d1;
	}
	return 0;
}

