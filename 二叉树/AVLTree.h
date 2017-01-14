#pragma once
#include "UserInfo.h"
#include <vector>
#include <math.h>
#include <stdlib.h>
class AVLTree
{
private:
	UserInfo *root;		//AVL树的根节点
public:


	void saveTreeToFile(string file);	//用前序遍历AVL树来储存树
	void showTreeToFile(string file);
	void destory();		//销毁AVL树
	void insert(string ID, string password);	//插入指定值的节点
	void remove(string ID);	//移除指定值的节点
	UserInfo* search(string ID);	//指定值的查找
	bool password_istrue(string ID, string password);
	void changePassword(string id, string password);
	string minimum();		//返回AVL中的最小值
	string maximum();		//返回AVL中的最大值
	int height();		//返回树的高度
	AVLTree();
	~AVLTree();
private:


	void destory(UserInfo* & pnode);

	int height(UserInfo* pnode);	//返回当前树的高度
//	int max(int a, int b);		//比较函数,没有使用函数库中函数

	UserInfo* insert(UserInfo* &pnode, string ID, string password);	//返回插入后的根节点
	UserInfo* remove(UserInfo* & pnode, string ID); //删除AVL树中节点pdel，并返回被删除的节点

	UserInfo* minimum(UserInfo*pnode)const;		//返回最小节点
	UserInfo* maximum(UserInfo*pnode)const;		//返回最大节点


	UserInfo* search(UserInfo* pnode, string ID) const;	//查找指定元素

	UserInfo* leftRotation(UserInfo* pnode);		//左旋操作
	UserInfo* rightRotation(UserInfo* pnode);		//右旋操作
	UserInfo* leftRightRotation(UserInfo* pnode);	//先左旋后右旋操作
	UserInfo* rightLeftRotation(UserInfo* pnode);	//先右旋后左旋操作

													/*以下函数调试程序使用*/
public:
//	void preOrder();	//用前序遍历AVL树
	void printtheTree();
	void dotreeholl();
private:
	void preOrder(ostream &out, UserInfo* pnode) const;
	std::vector<string> printTree;
	void bulidTree(UserInfo *T, int deep);
	int count = 0;
};
