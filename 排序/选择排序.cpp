#include <iostream>
#include <vector>
using namespace std;
void xs(vector <int > &v)
{
	int minn, temp;
	for (int i = 0; i < v.size() - 1; i++)
	{
		minn = i;
		for (int j = i + 1; j < v.size(); j++)
		{
			if (v[minn] > v[j])
				minn = j;
		}
		temp = v[i];
		v[i] = v[minn];
		v[minn] = temp;
	}
}
int main()
{
    return 0;
}