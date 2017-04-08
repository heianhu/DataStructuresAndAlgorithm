#include <iostream>
#define inf 1<<20
using namespace std;
int main()
{
	int e[10][10], dis[10], book[10], i, j, n, m, t1, t2, t3, u, v, min;
	cin >> n >> m;
	for (i = 1; i <= n; i++)	//初始化
		for (j = 1; j <= n; j++)
			if (i == j) e[i][j] = 0;
			else e[i][j] = inf;	
	for (i = 1; i <= m; i++)	//读入边
	{
		cin >> t1 >> t2 >> t3;
		e[t1][t2] = t3;
	}	
	for (i = 1; i <= n; i++)	//初始化dis数组，这里是1号顶点到其余各个顶点的初始路程
		dis[i] = e[1][i];
	for (i = 1; i <= n; i++)	//book数组初始化
		book[i] = 0;
	book[1] = 1;
	for (i = 1; i <= n - 1; i++)	//Dijkstra算法核心语句
	{
		//找到离1号顶点最近的顶点
		min = inf;
		for (j = 1; j <= n; j++)
		{
			if (book[j] == 0 && dis[j] < min)
			{
				min = dis[j];
				u = j;
			}
		}
		book[u] = 1;
		for (v = 1; v <= n; v++)
		{
			if (e[u][v] < inf)
			{
				if (dis[v] > dis[u] + e[u][v])
					dis[v] = dis[u] + e[u][v];
			}
		}
	}
	for (i = 1; i <= n; i++)	//输出最终的结果
		cout << dis[i] << " ";
	return 0;
}