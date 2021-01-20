/**
 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

 示例 1:

 输入: 1->2->3->4->5->NULL, k = 2
 输出: 4->5->1->2->3->NULL
 解释:
 向右旋转 1 步: 5->1->2->3->4->NULL
 向右旋转 2 步: 4->5->1->2->3->NULL
 示例 2:

 输入: 0->1->2->NULL, k = 4
 输出: 2->0->1->NULL
 解释:
 向右旋转 1 步: 2->0->1->NULL
 向右旋转 2 步: 1->2->0->NULL
 向右旋转 3 步: 0->1->2->NULL
 向右旋转 4 步: 2->0->1->NULL
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        ListNode tempHead = head;
        ListNode lastHead = new ListNode(-1);
        ListNode changeHead = head;
        // 遍历一次链表获取：1、长度；2、最后节点
        int listLength = 0;
        while (tempHead != null) {
            if (tempHead.next == null) {
                lastHead = tempHead;
            }
            listLength++;
            tempHead = tempHead.next;
        }
        if (listLength <= 1) {
            return head;
        }
        k %= listLength;
        if (k == 0) {
            return head;
        }
        tempHead = head;
        // 找到要换的节点的前一个节点
        int changeIndex = listLength - k - 1;
        while (changeIndex-- > 0) {
            changeHead = changeHead.next;
        }
        // 交换各个节点
        lastHead.next = tempHead;
        tempHead = changeHead.next;
        changeHead.next = null;
        return tempHead;
    }
}

