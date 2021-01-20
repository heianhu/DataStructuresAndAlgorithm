/**
 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



 示例 1：

 输入：nums = [1,2,3]
 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 示例 2：

 输入：nums = [0]
 输出：[[],[0]]


 提示：

 1 <= nums.length <= 10
 -10 <= nums[i] <= 10
 nums 中的所有元素 互不相同
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), result);
        return result;
    }

    void dfs(int[] nums, int index, List<Integer> resultTmp, List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(resultTmp));
            return;
        }
        // 不用当前数据用下一个
        dfs(nums, index + 1, resultTmp, result);

        // 用当前数据
        resultTmp.add(nums[index]);
        dfs(nums, index + 1, resultTmp, result);
        resultTmp.remove(resultTmp.size() - 1);
    }
}

