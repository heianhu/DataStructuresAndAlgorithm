#include "stdafx.h"
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cctype>
#include <cmath>
using namespace std;

//vector<int> f(vector<int> a, vector<int> b)
//{
//	vector<int> cal(a.size() + b.size(), 0);
//	for (int i = b.size() - 1; i >= 0; i--)
//	{
//		for (int j = a.size() + i, count = a.size(); count > 0; j--, count--)
//		{
//			cal[j] += a[j - i - 1] * b[i];
//		}
//	}
//	int carry = 0;
//	for (int i = a.size() + b.size() - 1; i >= 0; i--)
//	{
//		cal[i] += carry;
//		carry = cal[i] / 10;
//		cal[i] %= 10;
//	}
//	return cal;
//}

void printres(list<char> ans)
{
	list<char>::iterator iter;
	int flag = 1;
	iter = ans.begin();
	if (*iter == '-')
	{
		cout << *iter;
		iter++;
	}
	for (; iter != ans.end(); ++iter)
	{
		if (*iter == '0' && flag)
			continue;
		//cout << (*iter);
		else
		{
			flag = 0;
			cout << (*iter);
		}
	}
	if (flag == 1)
		cout << 0;
	//cout << endl;
}

list<char> Add(list<char> num1, list<char> num2)  //加法运算
{
	list<char> ans;
	list<char>::iterator iter1, iter2;
	iter1 = num1.begin();
	iter2 = num2.begin();
	int sign = 0;	//标记结果符号 

	int len1, len2, i, len, carry;
	len1 = num1.size();
	len2 = num2.size();
	if (len1 >= len2)	//补齐两个数的位数 
	{
		len = len1;
		for (i = 0; i < len1 - len2; i++)
			num2.push_front('0');
	}
	else
	{
		len = len2;
		for (i = 0; i < len2 - len1; i++)
			num1.push_front('0');
	}
	//printres(num1);
	//printres(num2);
	carry = 0;
	iter1 = num1.end();
	iter2 = num2.end();
	iter1--;
	iter2--;
	for (; (iter1 != num1.begin()) && (iter2 != num2.begin()); --iter1, --iter2)	//进行运算
	{
		i = (*iter1 - '0') + (*iter2 - '0') + carry;
		//cout << (*iter1 - '0') << " " << (*iter2 - '0') << " " << i << endl;
		ans.push_front((i % 10) + '0');
		carry = i / 10;
	}
	i = (*iter1 - '0') + (*iter2 - '0') + carry;
	//cout << (*iter1 - '0') << " " << (*iter2 - '0') << " " << i << endl;
	ans.push_front((i % 10) + '0');
	carry = i / 10;
	if (carry)
		ans.push_front(carry + '0');
	return ans;                                                    
}

list<char> Mul(list<char> num1, list<char> num2)  // 分治法求两大数的积
{
	list<char> ans;
	int sign = 0;
	int len1, len2, len;
	list<char>::iterator iter1, iter2, iter;
	list<char> high, low;
	list<char> anshigh, anslow;
	int th, tl;
	int i, j, k;
	//printres(num1);cout << endl;
	//printres(num2);cout << endl;
	if (num1.size() == 1 && num2.size() == 1)	//如果两数都已是一位数，则进行运算
	{
		th = *(num1.begin()) - '0';
		tl = *(num2.begin()) - '0';
		th *= tl;
		ans.push_front(th % 10 + '0');
		ans.push_front(th / 10 + '0');
		return ans;
	}
	else if (num1.size() == 1 && num2.size() > 1)	//如果num1位数大于1，则对Num1分治求积
	{
		if (*(num2.begin()) == '-')
		{
			sign = 1;
			num2.pop_front();
		}
		len2 = num2.size();
		if (len2 == 1)
		{
			ans = Mul(num1, num2);
			if (sign)
				ans.push_front('-');
		}
		else
		{
			for (iter = num2.begin(), i = 0; i < len2 / 2; i++, iter++)
			{
				high.push_back(*iter);
			}
			for (; iter != num2.end(); iter++)
			{
				low.push_back(*iter);
			}
			len = low.size();
			anshigh = Mul(num1, high);	//num1分为两部分，high,low 
			anslow = Mul(num1, low);
			for (i = 0; i < len; i++)
				anshigh.push_back('0');
			ans = Add(anshigh, anslow);	//合并结果
			if (sign)
				ans.push_front('-');
		}
		return ans;
	}
	else if (num2.size() == 1 && num1.size() > 1)	//如果num2位数大于1，则对Num2分治求积
	{
		if (*(num1.begin()) == '-')
		{
			sign = 1;
			num1.pop_front();
		}
		len1 = num1.size();
		if (len1 == 1)
		{
			ans = Mul(num1, num2);
			if (sign)
				ans.push_front('-');
		}
		else
		{
			for (iter = num1.begin(), i = 0; i < len1 / 2; i++, iter++)
			{
				high.push_back(*iter);
			}
			for (; iter != num1.end(); iter++)
			{
				low.push_back(*iter);
			}
			len = low.size();
			anshigh = Mul(num2, high);                 
			anslow = Mul(num2, low);
			for (i = 0; i < len; i++)
				anshigh.push_back('0');
			ans = Add(anshigh, anslow);                    
			if (sign)
				ans.push_front('-');
		}
		return ans;
	}                                                      
	else	//如果两数位数都大于1，则都运用分治 
	{
		list<char> num1high, num1low, num2high, num2low;
		int flag1 = 0, flag2 = 0;
		if (*(num1.begin()) == '-')
		{
			flag1 = 1;
			num1.pop_front();
		}
		if (*(num2.begin()) == '-')
		{
			flag2 = 1;
			num2.pop_front();
		}
		if ((flag1 == 1 && flag2 == 0) || (flag1 == 0 && flag2 == 1))  
		{
			sign = 1;
		}
		len1 = num1.size();
		len2 = num2.size();
		if (len1 == 1 || len2 == 1)	//如果有一个数是一位数，则直接递归调用
		{
			ans = Mul(num1, num2);
			if (sign)
				ans.push_front('-');
		}
		else
		{                                                
			for (iter = num1.begin(), i = 0; i < len1 / 2; iter++, i++)
				num1high.push_back(*iter);            
			for (; iter != num1.end(); iter++)
				num1low.push_back(*iter);                 
			for (iter = num2.begin(), i = 0; i < len2 / 2; iter++, i++)
				num2high.push_back(*iter);                  
			for (; iter != num2.end(); iter++)
				num2low.push_back(*iter);                    
			int a = (len1 + 1) / 2;
			int b = (len2 + 1) / 2;
			list<char> AC, AD, BC, BD;
			//printres(num2high);cout << endl;
			//printres(num2low);cout << endl;
			AC = Mul(num1high, num2high);                  //运用X=A*10^a + B; Y= C*10^b + D;
			AD = Mul(num1high, num2low);                   // X*Y = AC * 10 ^(a+b) + AD *10^a + BC * 10 ^b + BD公式求
			BC = Mul(num1low, num2high);
			BD = Mul(num1low, num2low);
			for (i = 0; i < a + b; i++)
				AC.push_back('0');
			for (i = 0; i < a; i++)
				AD.push_back('0');
			for (i = 0; i < b; i++)
				BC.push_back('0');
			ans = Add(AC, AD);
			ans = Add(ans, BC);
			ans = Add(ans, BD);                           
			if (sign)
				ans.push_front('-');
		}
		return ans;
	}
}

int main()
{
	//cout << "请输入被乘数:";
	//vector<int> a, b;
	//unsigned long long temp;
	//cin >> temp;
	//while (temp > 0)
	//{
	//	a.push_back(temp % 10);
	//	temp /= 10;
	//}
	//reverse(a.begin(), a.end());
	//cout << "请输入乘数:";
	//cin >> temp;
	//while (temp)
	//{
	//	b.push_back(temp % 10);
	//	temp /= 10;
	//}
	//reverse(b.begin(), b.end());
	//for (auto t : a)
	//	cout << t;
	//cout << "*";
	//for (auto t : b)
	//	cout << t;
	//cout << "=";
	//bool flag = 0; 
	//for (auto t : f(a, b))
	//{
	//	if (t != 0)
	//		flag = 1;
	//	if (!flag)
	//		continue;
	//	cout << t;
	//}
	//cout << endl;

	cout << "请输入被乘数:";
	string input;
	cin >> input;
	list<char> a;
	for (int i = 0; i < input.length(); i++)
		a.push_back(input[i]);
	input = "";
	cout << "请输入乘数:";
	cin >> input;
	list<char> b;
	for (int i = 0; i < input.length(); i++)
		b.push_back(input[i]);
	auto res = Mul(a, b);
	for (auto t : a)
		cout << t;
	cout << "*";
	for (auto t : b)
		cout << t;
	cout << "=";
	printres(res);
	cout << endl;
    return 0;
}






























