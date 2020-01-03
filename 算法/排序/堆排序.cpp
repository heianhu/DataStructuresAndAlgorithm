//第一次实现堆排序，所以写了一些注释以及实例
#include <time.h>
#include <iostream>
#include <vector>
using namespace std;
void MinHeapify(vector<int> &arry, int size, int element)
{
	int lchild = element * 2 + 1, rchild = lchild + 1;//左右子树
	while (rchild < size)//子树均在范围内
	{
		if (arry[element] <= arry[lchild] && arry[element] <= arry[rchild])//如果比左右子树都小，完成整理
		{
			return;
		}
		if (arry[lchild] <= arry[rchild])//如果左边最小
		{
			swap(arry[element], arry[lchild]);//把左面的提到上面
			element = lchild;//循环时整理子树
		}
		else//否则右面最小
		{
			swap(arry[element], arry[rchild]);//同理
			element = rchild;
		}
		lchild = element * 2 + 1;
		rchild = lchild + 1;//重新计算子树位置
	}
	if (lchild < size&&arry[lchild] < arry[element])//只有左子树且子树小于自己
	{
		swap(arry[lchild], arry[element]);
	}
	return;
}

void HeapSort(vector<int> &arry, int size)
{
	int i;
	for (i = size - 1; i >= 0; i--)//从子树开始整理树
	{
		MinHeapify(arry, size, i);
	}
	while (size > 0)//拆除树
	{
		swap(arry[size - 1], arry[0]);//将根（最小）与数组最末交换
		size--;//树大小减小
		MinHeapify(arry, size, 0);//整理树
	}
	return;
}

void RemoveRep(vector<int> &v)
{
	int temp;
	int n = v.size();
	for (int i = 0; i < n - 1; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (v[i] == v[j])
			{
				v[j] = v[n - 1];
				v.pop_back();
				j--;
				n--;
			}
		}
	}
}

int main()
{
	vector<int> s;

	srand(time(0));

	for (int i = 0; i < 10; i++)
	{
		s.push_back(1 + rand() % 10);
	}
	RemoveRep(s);
	for (int i = 0; i < s.size(); i++)
	{
		cout << s[i] << " ";
	}
	cout << endl << s.size() << endl;

	HeapSort(s, s.size());
	for (int i = 0; i < s.size(); i++)
	{
		cout << s[i] << " ";
	}
	return 0;
}
