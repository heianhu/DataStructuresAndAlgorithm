/**
 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

 candidates 中的每个数字在每个组合中只能使用一次。

 说明：

 所有数字（包括目标数）都是正整数。
 解集不能包含重复的组合。
 示例 1:

 输入: candidates = [10,1,2,7,6,1,5], target = 8,
 所求解集为:
 [
 [1, 7],
 [1, 2, 5],
 [2, 6],
 [1, 1, 6]
 ]
 示例 2:

 输入: candidates = [2,5,2,1,2], target = 5,
 所求解集为:
 [
 [1,2,2],
 [5]
 ]
 */

import java.util.*;


class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        // 先做一次排序，方便后面跳过已经使用过的数字
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        dfs(candidates, result, new ArrayList<>(), target, 0);

        return result;
    }

    void dfs(int[] candidates, List<List<Integer>> result, List<Integer> tmpList, int target, int index) {
        if (target == 0) {
            result.add(new ArrayList<>(tmpList));
            return;
        }
        if (index == candidates.length) {
            return;
        }
        // 使用当前的这个数字
        if (target - candidates[index] >= 0) {
            tmpList.add(candidates[index]);
            dfs(candidates, result, tmpList, target - candidates[index], index + 1);
            tmpList.remove(tmpList.size() - 1);
        }
        // 跳过当前数字
        while (index + 1 < candidates.length && candidates[index] == candidates[index + 1]) {
            index++;
        }
        dfs(candidates, result, tmpList, target, index + 1);
    }
}

