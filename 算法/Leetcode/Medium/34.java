/**
 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

 如果数组中不存在目标值 target，返回 [-1, -1]。

 进阶：

 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


 示例 1：

 输入：nums = [5,7,7,8,8,10], target = 8
 输出：[3,4]
 示例 2：

 输入：nums = [5,7,7,8,8,10], target = 6
 输出：[-1,-1]
 示例 3：

 输入：nums = [], target = 0
 输出：[-1,-1]


 提示：

 0 <= nums.length <= 105
 -109 <= nums[i] <= 109
 nums 是一个非递减数组
 -109 <= target <= 109
 */

import java.util.*;



class Solution {
    public int[] searchRange(int[] nums, int target) {
        // 先用二分查找找到一个相等的点
        int left = 0;
        int right = nums.length - 1;
        int isFind = -1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                isFind = mid;
                break;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        left = isFind;
        right = isFind;
        // 向两边扩散坐标
        if (isFind != -1) {
            // 找到第一个不同的坐标，之后回退一个
            while (left >= 0 && nums[isFind] == nums[left]) {
                left--;
            }
            left++;
            while (right < nums.length && nums[isFind] == nums[right]) {
                right++;
            }
            right--;
        }
        return new int[] {left, right};
    }
}

