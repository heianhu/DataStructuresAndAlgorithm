#include<iostream>  
#include<stack>  
using namespace std;
int main(void)
{
	stack<double>s;
	for (int i = 0; i < 10; i++)
		s.push(i);
	while (!s.empty())
	{
		cout << s.top() << endl;
		s.pop();
	}
	cout << "栈内的元素的个数为：" << s.size() << endl;
	return 0;
}