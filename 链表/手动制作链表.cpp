#include <iostream>
using namespace std;
struct student  //定义自定义数组类型 
{
	int num;
	float score;
	student *next;
};
int main(int argc, char** argv) //主函数 
{
	student *creat(void);  //建立链表 
	void print(student *head);  //输出链表 
	student *insert(student *head, student *stu);  //插入链表节点 
	student *del(student *head, int num);  //删除节点 
	student *head, *stu;
	int del_num, Features;
	cout << "请输入链表：" << endl;
	head = creat();  //输入链表并且返回首地址 
	print(head);  //输出所有节点 
	cout << endl << "请选择功能，输入0退出程序" << endl << "1:删除学生" << endl << "2:插入学生" << endl;
	while (cin >> Features)
	{
		if (Features == 1)
		{
			cout << "请输入要删除的学生的学号,输入0时退出删除";
			cin >> del_num;
			while (del_num != 0)
			{
				head = del(head, del_num);
				print(head);
				cout << "请输入要删除的学生的学号,输入0时退出删除";
				cin >> del_num;
			}
		}
		if (Features == 2)
		{
			cout << "请输入要插入的学生信息(学号和分数)，当学号为0时退出插入";
			stu = new student;
			cin >> stu->num >> stu->score;
			while (stu->num != 0)
			{
				head = insert(head, stu);
				print(head);
				cout << "请输入要插入的学生信息(学号和分数)，当学号为0时退出插入";
				stu = new student;
				cin >> stu->num >> stu->score;
			}
		}
		if (Features == 0) return 0;
	}
	return 0;
}
int n;  //定义全局变量n 
student *creat(void)  //建立链表的函数，此函数带回一个指向链表头的指针 
{
	student *head, *p1, *p2;
	n = 0;
	p1 = p2 = new student;  //使p1,p2指向一个新开辟的新单元 
	cin >> p1->num >> p1->score;
	head = NULL;
	while (p1->num != 0)  //判断是否结束 
	{
		n++;
		if (n == 1) head = p1;  //将头地址赋值 
		else p2->next = p1;   //重点* 
		p2 = p1;
		p1 = new student;  //*重点 
		cin >> p1->num >> p1->score;
	}
	p2->next = NULL;
	return (head);
}
void print(student *head)  //输出链表 
{
	student *p;
	cout << endl << n << "个学生为：" << endl;
	p = head;
	if (head != NULL)
		while (p != NULL)
		{
			cout << p->num << " " << p->score << endl;
			p = p->next;
		}
}
student *insert(student *head, student *stu)  //插入链表节点 
{
	student *p0, *p1, *p2=NULL;
	p1 = head;
	p0 = stu;
	if (head == NULL)
	{
		head = p0;
		p0->next = NULL;
	}
	else
	{
		while ((p0->num > p1->num) && (p1->num != NULL))
		{
			p2 = p1;
			p1 = p1->next;
		}
		if (p0->num <= p1->num)
		{
			if (head == p1) head = p0;
			else p2->next = p0;
			p0->next = p1;
		}
		else
		{
			p1->next = p0;
			p0->next = NULL;
		}
	}
	n = n + 1;
	return (head);
}
student *del(student *head, int num)  //删除链表中的一个节点 
{
	student *p1, *p2=NULL;
	if (head == NULL)
	{
		cout << "链表为空" << endl;
		return (head);
	}
	p1 = head;
	while (num != p1->num&&p1->next != NULL)
	{
		p2 = p1;
		p1 = p1->next;
	}
	if (num == p1->num)
	{
		if (p1 == head) head = p1->next;
		else p2->next = p1->next;
		cout << "删除：" << num << endl;
		n--;
	}
	else cout << "在链表中没有找到" << num << endl;
	return (head);
}