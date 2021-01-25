/**
 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

 说明:
 1 ≤ m ≤ n ≤ 链表长度。

 示例:

 输入: 1->2->3->4->5->NULL, m = 2, n = 4
 输出: 1->4->3->2->5->NULL
 */

import java.util.*;


class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) {
            return null;
        }
        ListNode preNode = null;
        ListNode currNode = head;

        // 找到要换节点的前一个
        for (int i = 0; i < m - 1; i++) {
            preNode = currNode;
            currNode = currNode.next;
        }
        ListNode preStartNode = preNode;
        ListNode endNode = currNode;

        // 将中间的节点反转
        ListNode tmpNode;
        for (int i = 0; i < n - m + 1; i++) {
            tmpNode = currNode.next;
            currNode.next = preNode;
            preNode = currNode;
            currNode = tmpNode;
        }

        // 连接节点
        if (preStartNode != null) {
            preStartNode.next = preNode;
        } else {
            head = preNode;
        }

        endNode.next = currNode;
        return head;
    }
}

