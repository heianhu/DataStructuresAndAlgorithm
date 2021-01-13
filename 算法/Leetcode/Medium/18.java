/**
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
 */

import java.util.*;


class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            for (int j = i + 1; j < nums.length - 2; j++) {
                int startPoint = j + 1;
                int endPoint = nums.length - 1;

                while (startPoint < endPoint) {
                    int sum = nums[i] + nums[j] + nums[startPoint] + nums[endPoint];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[startPoint], nums[endPoint]));
                    }

                    if (sum > target) {
                        while (startPoint < endPoint && nums[endPoint] == nums[endPoint - 1]) {
                            endPoint--;
                        }
                        endPoint--;
                    } else {
                        while (startPoint < endPoint && nums[startPoint] == nums[startPoint + 1]) {
                            startPoint++;
                        }
                        startPoint++;
                    }

                }
                while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
                    j++;
                }
            }
            while (i + 1 < nums.length && nums[i] == nums[i + 1]) {
                i++;
            }
        }

        return result;
    }
}
