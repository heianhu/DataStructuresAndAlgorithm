/**
 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。



 示例 1：

 输入：nums = [1,1,2]
 输出：
 [[1,1,2],
 [1,2,1],
 [2,1,1]]
 示例 2：

 输入：nums = [1,2,3]
 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


 提示：

 1 <= nums.length <= 8
 -10 <= nums[i] <= 10
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        dfs(nums, 0, nums.length, result);
        return new ArrayList<>(result);
    }

    void dfs(int[] nums, int left, int right, Set<List<Integer>> result) {
        if (left == right) {
            result.add(Arrays.stream(nums).boxed().collect(Collectors.toList()));
        }
        for (int i = left; i < right; i++) {
            if (nums[left] == nums[i] && left != i) {
                continue;
            }
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

