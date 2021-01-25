/**
 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

 说明：解集不能包含重复的子集。

 示例:

 输入: [1,2,2]
 输出:
 [
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
 ]
 */

import java.util.*;


class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        List<Integer> resultTmp = new ArrayList<>();
        Arrays.sort(nums);
        dfs(result, resultTmp, nums, 0);
        return new ArrayList<>(result);
    }

    void dfs(Set<List<Integer>> result, List<Integer> resultTmp, int[] nums, int index) {
        if (index == nums.length) {
            result.add(new ArrayList<>(resultTmp));
            return;
        }
        // 用当前的值
        resultTmp.add(nums[index]);
        dfs(result, resultTmp, nums, index + 1);
        resultTmp.remove(resultTmp.size() - 1);
        // 不用当前的值
        dfs(result, resultTmp, nums, index + 1);
    }
}

