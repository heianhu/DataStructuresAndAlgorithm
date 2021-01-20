/**
 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

 示例:

 输入: [1,2,3]
 输出:
 [
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
 ]
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, nums.length, result);
        return result;
    }

    void dfs(int[] nums, int left, int right, List<List<Integer>> result) {
        if (left == right) {
            result.add(Arrays.stream(nums).boxed().collect(Collectors.toList()));
        }
        for (int i = left; i < right; i++) {
            swap(nums, left, i);
            dfs(nums, left + 1, right, result);
            swap(nums, left, i);
        }
    }

    void swap(int[] nums, int left, int right) {
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
    }
}

