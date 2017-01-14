//直接套用以前学习的模版
#include<iostream>  
using namespace std;  
  
int a[11][11];  
bool visited[11];  
  
void store_graph()  //邻接矩阵存储图  
{  
    int i,j;  
  
    for(i=1;i<=10;i++)  
        for(j=1;j<=10;j++)  
            cin>>a[i][j];  
}  
  
void dfs_graph()    //深度遍历图  
{  
    void dfs(int v);  
  
    memset(visited,false,sizeof(visited));  
  
    for(int i=1;i<=10;i++)  //遍历每个顶点是为了防止图不连通时无法访问每个顶点  
        if(visited[i]==false)  
            dfs(i);  
}  
  
void dfs(int v)  //深度遍历顶点  
{  
    int Adj(int x);  
  
    cout<<v<<" ";  //访问顶点v  
    visited[v]=true;  
  
    int adj=Adj(v);  
    while(adj!=0)  
    {  
        if(visited[adj]==false)     
            dfs(adj);      //递归调用是实现深度遍历的关键所在  
  
        adj=Adj(v);  
    }  
}  
  
int Adj(int x)   //求邻接点  
{  
    for(int i=1;i<=10;i++)  
        if(a[x][i]==1 && visited[i]==false)  
            return i;  
  
    return 0;  
}  
  
int main()  
{  
    cout<<"初始化图:"<<endl;  
    store_graph();  
  
    cout<<"dfs遍历结果:"<<endl;  
    dfs_graph();  
  
    return 0;  
}  