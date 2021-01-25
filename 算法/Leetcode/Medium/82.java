/**
 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

 示例 1:

 输入: 1->2->3->3->4->4->5
 输出: 1->2->5
 示例 2:

 输入: 1->1->1->2->3
 输出: 2->3
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode resultHead = new ListNode(-1, head);
        ListNode curPoint = head.next;
        ListNode prePoint = head;
        ListNode prePrePoint = resultHead;
        boolean isDuplicate = false;
        while (curPoint != null) {
            if (curPoint.val == prePoint.val) {
                isDuplicate = true;
                prePoint.next = curPoint.next;
            } else {
                if (isDuplicate) {
                    prePrePoint.next = prePoint.next;
                } else {
                    prePrePoint = prePoint;
                }
                prePoint = prePoint.next;
                isDuplicate = false;
            }
            curPoint = curPoint.next;
        }
        if (isDuplicate) {
            prePrePoint.next = prePoint.next;
        }
        return resultHead.next;
    }
}

