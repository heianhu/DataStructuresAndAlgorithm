#include <iostream>
#include <vector>
using namespace std;
void ks(vector<int> &v, int left, int right)
{
	int t, temp;
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
		{
			t = v[i];
			v[i] = v[j];
			v[j] = t;
		}
	}
	v[left] = v[i];
	v[i] = temp;
	ks(v, left, i - 1);
	ks(v, i + 1, right);
}
int main()
{
    return 0;
}
