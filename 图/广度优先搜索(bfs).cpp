#include<iostream>  
#include<queue>      
using namespace std;

int a[11][11];
bool visited[11];

void store_graph()
{
	for (int i = 1; i <= 10; i++)
		for (int j = 1; j <= 10; j++)
			cin >> a[i][j];
}

void bfs_graph()
{
	void bfs(int v);

	memset(visited, false, sizeof(visited));

	for (int i = 1; i <= 10; i++)
		if (visited[i] == false)
			bfs(i);
}

void bfs(int v)
{
	int Adj(int x);

	queue<int> myqueue;
	int adj, temp;

	cout << v << " ";
	visited[v] = true;
	myqueue.push(v);

	while (!myqueue.empty())    //队列非空表示还有顶点未遍历到  
	{
		temp = myqueue.front();  //获得队列头元素  
		myqueue.pop();         //头元素出对  

		adj = Adj(temp);
		while (adj != 0)
		{
			if (visited[adj] == false)
			{
				cout << adj << " ";
				visited[adj] = true;
				myqueue.push(adj);   //进对  
			}

			adj = Adj(temp);
		}
	}
}

int Adj(int x)
{
	for (int i = 1; i <= 10; i++)
		if (a[x][i] == 1 && visited[i] == false)
			return i;

	return 0;
}

int main()
{
	cout << "初始化图:" << endl;
	store_graph();

	cout << "bfs遍历结果:" << endl;
	bfs_graph();

	return 0;
}