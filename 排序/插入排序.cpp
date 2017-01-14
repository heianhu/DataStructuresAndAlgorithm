#include <iostream>
#include <vector>
using namespace std;
void cs(vector<int> &v)
{
	int temp;
	for (int i = 1; i < v.size(); i++)
	{
		temp = v[i];
		for (int j = i - 1; j >= 0; j--)
		{
			if (v[j] > temp)
			{
				if (j == 0)
				{
					v[j + 1] = v[j];
					v[j] = temp;
				}
				else
				{
					v[j + 1] = v[j];
				}
			}
			else if (v[j] <= temp)
			{
				v[j + 1] = temp;
				break;
			}
		}
	}
}
int main()
{
    return 0;
}