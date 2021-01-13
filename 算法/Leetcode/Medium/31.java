/**
 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

 必须 原地 修改，只允许使用额外常数空间。



 示例 1：
 输入：nums = [1,2,3]
 输出：[1,3,2]

 示例 2：
 输入：nums = [3,2,1]
 输出：[1,2,3]

 示例 3：
 输入：nums = [1,1,5]
 输出：[1,5,1]

 示例 4：
 输入：nums = [1]
 输出：[1]


 提示：

 1 <= nums.length <= 100
 0 <= nums[i] <= 100
 */

import java.util.*;



class Solution {
    public void nextPermutation(int[] nums) {
        int left = nums.length - 2;
        int right = nums.length - 1;
        // 从右往左找到比较小的数
        while (left >= 0 && nums[left] >= nums[left + 1]) {
            left--;
        }
        // 确保数组长度大于1
        if (left >= 0) {
            // 找到一个比之前找到的数较大的数
            while (right >= 0 && nums[right] <= nums[left]) {
                right--;
            }
            // 做交换
            swap(nums, left, right);
        }
        // 将做交换的left的右端做反转
        // 没找到时做反转也会出现最小字典序
        reverse(nums, left + 1);
    }

    void reverse(int[] nums, int left) {
        int right = nums.length - 1;
        while (left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
    }

    void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

