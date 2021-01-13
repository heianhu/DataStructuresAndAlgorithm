/**
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
 */



import java.util.*;


class Solution {
    public List<String> generateParenthesis(int n) {
        int stringCount = n * 2;
        Set<String> result = new HashSet<>();
        if (n == 0) {
            return new ArrayList<>();
        }
        result.add("(");
        for (int i = 1; i < stringCount; i++) {
            Set<String> tmp = new HashSet<>();
            result.forEach(str -> {
                // 计算当前字符串有几个做括号和右括号
                int left = 0;
                int right = 0;
                for (int j = 0; j < str.length(); j++) {
                    if (str.charAt(j) == '(') {
                        left++;
                    } else {
                        right++;
                    }
                }
                // 可以加"("的情况
                if (left < n) {
                    tmp.add(str + "(");
                }
                // 可以加")"的情况
                if (right < left) {
                    tmp.add(str + ")");
                }
            });
            result = tmp;
        }
        return new ArrayList<>(result);
    }
}
