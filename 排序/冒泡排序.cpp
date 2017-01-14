#include <iostream>
#include <vector>
using namespace std;
void ms(vector<int> &v)
{
	int k = v.size();
	int temp;
	bool flag;
	flag = true;
	while (flag)
	{
		flag = false;
		for (int j = 1; j < k; j++)
			if (v[j - 1] > v[j])
			{
				temp = v[j - 1];
				v[j - 1] = v[j];
				v[j] = temp;
				flag = true;
			}
		k--;
	}
}
int main()
{
	return 0;
}