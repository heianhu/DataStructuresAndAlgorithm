#include "stdafx.h"
#include "AVLTree.h"
#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
AVLTree::AVLTree() :root(NULL)
{
}


AVLTree::~AVLTree()
{
	destory(root);
}

// int AVLTree::max(int a, int b)
// {
// 	return a > b ? a : b;
// }

void AVLTree::insert(string ID, string password)
{
	insert(root, ID, password);
}

UserInfo * AVLTree::insert(UserInfo *& pnode, string ID, string password)
{

	if (pnode == NULL)	//寻找到插入的位置
	{
		pnode = new UserInfo(ID, password, NULL, NULL);
	}
	else if (ID > pnode->getID())	//插入值比当前结点值大，插入到当前结点的右子树上
	{
		pnode->rchild = insert(pnode->rchild, ID, password);
		if (height(pnode->rchild) - height(pnode->lchild) == 2) //插入后出现失衡
		{
			if (ID > pnode->rchild->getID()) //情况一：插入右子树的右节点，进行左旋
				pnode = leftRotation(pnode);
			else if (ID < pnode->rchild->getID())  //情况三：插入右子树的左节点,进行先右再左旋转
				pnode = rightLeftRotation(pnode);
		}
	}
	else if (ID < pnode->getID()) //插入值比当前节点值小，插入到当前结点的左子树上
	{
		pnode->lchild = insert(pnode->lchild, ID, password);
		if (height(pnode->lchild) - height(pnode->rchild) == 2) //如果插入导致失衡
		{
			if (ID < pnode->lchild->getID())		//情况二：插入到左子树的左孩子节点上，进行右旋
				pnode = rightRotation(pnode);
			else if (ID > pnode->lchild->getID())
				pnode = leftRightRotation(pnode);//情况四：插入到左子树的右孩子节点上，进行先左后右旋转
		}
	}
	pnode->setHeight(max(height(pnode->lchild), height(pnode->rchild)) + 1);
	return pnode;
}

void AVLTree::remove(string ID)
{
	root = remove(root, ID);
}

UserInfo * AVLTree::remove(UserInfo *& pnode, string ID)
{
	if (pnode != NULL)
	{
		if (ID == pnode->getID())			//找到删除的节点
		{
			if (pnode->lchild != NULL&&pnode->rchild != NULL)		//若左右都不为空
			{
				if (height(pnode->lchild) > height(pnode->rchild))		//左子树比右子树高
				{
					//使用左子树最大节点来代替被删节点，而删除该最大节点
					UserInfo* ppre = maximum(pnode->lchild);		//左子树最大节点
					pnode->setID(ppre->getID());							//将最大节点的值覆盖当前结点
					pnode->lchild = remove(pnode->lchild, ppre->getID());	//递归地删除最大节点
				}
				else
				{
					//使用最小节点来代替被删节点，而删除该最小节点
					UserInfo* psuc = minimum(pnode->rchild);		//右子树的最小节点
					pnode->setID(psuc->getID());								//将最小节点值覆盖当前结点
					pnode->rchild = remove(pnode->rchild, psuc->getID());	//递归地删除最小节点
				}

			}
			else
			{
				UserInfo * ptemp = pnode;
				if (pnode->lchild != NULL)
					pnode = pnode->lchild;
				else if (pnode->rchild != NULL)
					pnode = pnode->rchild;
				delete ptemp;
				return NULL;
			}

		}
		else if (ID > pnode->getID())		//要删除的节点比当前节点大，则在右子树进行删除
		{
			pnode->rchild = remove(pnode->rchild, ID);
			if (height(pnode->lchild) - height(pnode->rchild) == 2) //删除右子树节点导致不平衡:相当于情况二或情况四
			{
				if (height(pnode->lchild->rchild) > height(pnode->lchild->lchild))
					pnode = leftRightRotation(pnode);				//相当于情况四
				else
					pnode = rightRotation(pnode);					//相当于情况二
			}
		}
		else if (ID < pnode->getID())		//要删除的节点比当前节点小，则在左子树进行删除
		{
			pnode->lchild = remove(pnode->lchild, ID);
			if (height(pnode->rchild) - height(pnode->lchild) == 2)  //删除左子树节点导致不平衡：相当于情况三或情况一
			{
				if (height(pnode->rchild->lchild) > height(pnode->rchild->rchild))
					pnode = rightLeftRotation(pnode);
				else
					pnode = leftRotation(pnode);
			}
		}
		return pnode;
	}
	return NULL;
}

void AVLTree::destory()
{
	destory(root);
}

void AVLTree::destory(UserInfo *& pnode)
{
	if (pnode != NULL)
	{
		destory(pnode->lchild);
		destory(pnode->rchild);
		delete pnode;
		pnode = NULL;
	}
}

UserInfo * AVLTree::search(string ID)
{
	return search(root, ID);;
}

bool AVLTree::password_istrue(string ID, string password)
{
	UserInfo *Find = search(ID);
	if (Find!=NULL&&Find->getPassword()==password)
	{
		return true;
	}
	return false;
}

void AVLTree::changePassword(string id, string password)
{
	UserInfo *Find = search(id);
	Find->setPassword(password);
}

UserInfo * AVLTree::search(UserInfo * pnode, string ID) const
{
	while (pnode != NULL)
	{
		if (pnode->getID() == ID)
			return pnode;
		else if (ID > pnode->getID())
			pnode = pnode->rchild;
		else
			pnode = pnode->lchild;
	}
	return NULL;
}

UserInfo * AVLTree::minimum(UserInfo * pnode) const
{
	if (pnode != NULL)
	{
		while (pnode->lchild != NULL)
			pnode = pnode->lchild;
		return pnode;
	}
	return NULL;
}

string AVLTree::minimum()
{
	UserInfo* presult = minimum(root);
	if (presult != NULL)
		return presult->getID();
}

UserInfo * AVLTree::maximum(UserInfo*pnode)const
{
	if (pnode != NULL)
	{
		while (pnode->rchild != NULL)
			pnode = pnode->rchild;
		return pnode;
	}
	return NULL;
}

string AVLTree::maximum()
{
	UserInfo* presult = maximum(root);
	if (presult != NULL)
		return presult->getID();
}

int AVLTree::height(UserInfo* pnode)
{
	if (pnode != nullptr)
	{
		return pnode->getHeight();
	}
	return 0;																//如果是空树，高度为0
};

int AVLTree::height()
{
	return height(root);
};

//pnode为最小失衡子树的根节点
//返回旋转后的根节点
UserInfo* AVLTree::leftRotation(UserInfo* proot)	//左旋
{
	UserInfo* prchild = proot->rchild;
	proot->rchild = prchild->lchild;
	prchild->lchild = proot;

	proot->setHeight(max(height(proot->lchild), height(proot->rchild)) + 1);		//更新节点的高度值
	prchild->setHeight(max(height(prchild->lchild), height(prchild->rchild)) + 1);	//更新节点的高度值

	return prchild;
};

UserInfo* AVLTree::rightRotation(UserInfo*proot)	//右旋
{
	UserInfo* plchild = proot->lchild;
	proot->lchild = plchild->rchild;
	plchild->rchild = proot;

	proot->setHeight(max(height(proot->lchild), height(proot->rchild)) + 1);     //更新节点的高度值
	plchild->setHeight(max(height(plchild->lchild), height(plchild->rchild)) + 1); //更新节点的高度值

	return plchild;
};

UserInfo* AVLTree::leftRightRotation(UserInfo* proot)	//先左后右
{
	proot->lchild = leftRotation(proot->lchild);
	return rightRotation(proot);
};

UserInfo* AVLTree::rightLeftRotation(UserInfo* proot)	//先右后左
{
	proot->rchild = rightRotation(proot->rchild);
	return leftRotation(proot);
};

void AVLTree::saveTreeToFile(string file)
{
	ofstream fout(file);
	preOrder(fout,root);
	fout.close();

}


/*以下函数调试程序使用*/
// void AVLTree::preOrder()
// {
// 	preOrder(root);
// }

void AVLTree::preOrder(ostream &out,UserInfo * pnode) const
{
	if (pnode != NULL)
	{
		out << pnode->getID() <<" "<< pnode->getPassword() << endl;
		//cout << pnode->getID() << endl;
		preOrder(out,pnode->lchild);
		preOrder(out,pnode->rchild);
	}
}

void AVLTree::dotreeholl()
{
	printTree.resize(height() * 2);
	for (int i = 0; i < printTree.size(); i++)
	{
		printTree[i].assign(int(pow(2, height() - 1)) * 4, ' ');
	}
}

void AVLTree::bulidTree(UserInfo *T, int deep)
{
	if (NULL != T)
	{
		bulidTree(T->lchild, deep + 1);
		printTree[deep * 2].insert(count, T->getID());
		if (NULL != T->lchild)
			printTree[deep * 2 + 1][count] = '/';
		if (NULL != T->rchild)
			printTree[deep * 2 + 1][count + 1] = '\\';
		count += 2;
		bulidTree(T->rchild, deep + 1);
	}
}

void AVLTree::printtheTree()
{
	bulidTree(root, 0);
	for (int i = 0; i < printTree.size(); i++)
	{
		cout << printTree[i] << endl;
	}
}

void AVLTree::showTreeToFile(string file)
{
	count = 0;
	for (int i = 0; i < printTree.size(); i++)
		printTree[i] = "";
	ofstream fout(file);
	fout << "这个小秘密就是树状展示出现有的账户,当然密码就没有咯~" << endl;
	dotreeholl();
	bulidTree(root, 0);
	for (int i = 0; i < printTree.size(); i++)
	{
		fout << printTree[i] << endl;
	}
	fout.close();
}