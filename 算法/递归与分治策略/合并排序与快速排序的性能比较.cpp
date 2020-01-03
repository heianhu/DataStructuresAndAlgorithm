#include "stdafx.h"
#include <iostream>
#include <vector>
#include <windows.h>
#include <fstream>
#include <mmsystem.h>
#pragma comment(lib, "winmm.lib") 
#define MAX 2<<24
using namespace std;

void ks(vector<int> &v, int left, int right)
{
	int temp;
	if (left > right)
		return;

	temp = v[left];
	int i = left;
	int j = right;
	while (i < j)
	{

		while (v[j] >= temp && i < j)
			j--;

		while (v[i] <= temp && i < j)
			i++;

		if (i < j)
			swap(v[i], v[j]);
	}
	swap(v[left], v[i]);
	ks(v, left, i - 1);
	ks(v, i + 1, right);
}

void hb(vector<int> &v, int left, int mid, int right)
{
	vector<int> l, r;
	for (int i = left; i <= mid; i++)
		l.push_back(v[i]);
	l.push_back(MAX);
	for (int i = mid + 1; i <= right; i++)
		r.push_back(v[i]);
	r.push_back(MAX);
	auto pl = l.begin(), pr = r.begin();
	for (int k = left; k <= right; k++)
		if (*pl > *pr)
			v[k] = *pr++;
		else
			v[k] = *pl++;
}

void hs(vector<int> &v, int left, int right)
{
	int mid = (left + right) / 2;
	if (left<right)
	{
		hs(v, left, mid);
		hs(v, mid + 1, right);
		hb(v, left, mid, right);
	}
}

int main()
{
	ifstream fin("..\\data.txt");
	unsigned int time;
	cout << "正在从：\"..\\data.txt\"导入数据";
	vector<int> temp;
	int t;
	while (fin >> t)
		temp.push_back(t);
	fin.close();
	cout << endl << "导入的数据为:" << endl;
	for (auto a : temp)
		cout << a << " ";
	cout << endl;
	vector<int> qs(temp), ms(temp);
	cout << "快速排序后的数据为:" << endl;
	time = ::timeGetTime();
	ks(qs, 0, qs.size() - 1);
	time = ::timeGetTime() - time;
	for (auto a : qs)
		cout << a << " ";
	cout << endl << "快速排序所用时间为：" << time << "毫秒" << endl;
	cout << "合并排序后的数据为:" << endl;
	time = ::timeGetTime();
	hs(ms, 0, ms.size() - 1);
	time = ::timeGetTime() - time;
	for (auto a : ms)
		cout << a << " ";
	cout << endl << "合并排序所用时间为：" << time << "毫秒" << endl;
	return 0;
}
