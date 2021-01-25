/**
 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

 你应当保留两个分区中每个节点的初始相对位置。



 示例：

 输入：head = 1->4->3->2->5->2, x = 3
 输出：1->2->2->4->3->5
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode leftPoint = new ListNode(-1);
        ListNode rightPoint = new ListNode(-1);
        ListNode left = leftPoint;
        ListNode right = rightPoint;
        while (head != null) {
            if (head.val < x) {
                left.next = head;
                left = left.next;
            } else {
                right.next = head;
                right = right.next;
            }
            head = head.next;
        }
        left.next = rightPoint.next;
        right.next = null;
        return leftPoint.next;
    }
}

