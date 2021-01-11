/**
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

Map<Character, List<String>> stringListMap = new HashMap<>();
stringListMap.put('2', Arrays.asList("a", "b", "c"));
stringListMap.put('3', Arrays.asList("d", "e", "f"));
stringListMap.put('4', Arrays.asList("g", "h", "i"));
stringListMap.put('5', Arrays.asList("j", "k", "l"));
stringListMap.put('6', Arrays.asList("m", "n", "o"));
stringListMap.put('7', Arrays.asList("p", "q", "r", "s"));
stringListMap.put('8', Arrays.asList("t", "u", "v"));
stringListMap.put('9', Arrays.asList("w", "x", "y", "z"));

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 */



import java.util.*;


class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        // 对应表
        Map<Character, List<String>> stringListMap = new HashMap<>();
        stringListMap.put('2', Arrays.asList("a", "b", "c"));
        stringListMap.put('3', Arrays.asList("d", "e", "f"));
        stringListMap.put('4', Arrays.asList("g", "h", "i"));
        stringListMap.put('5', Arrays.asList("j", "k", "l"));
        stringListMap.put('6', Arrays.asList("m", "n", "o"));
        stringListMap.put('7', Arrays.asList("p", "q", "r", "s"));
        stringListMap.put('8', Arrays.asList("t", "u", "v"));
        stringListMap.put('9', Arrays.asList("w", "x", "y", "z"));
        if (digits.length() < 1) {
            return result;
        }
        // 遍历号码
        // 第一个号码的强行塞入
        result.addAll(stringListMap.get(digits.charAt(0)));
        // 遍历后面的号码
        for (int i = 1; i < digits.length(); i++) {
            List<String> tmp = new ArrayList<>();
            // 遍历已有结果
            for (String tmpResult : result) {
                // 将已有结果和新的号码对应的字母拼接
                stringListMap.get(digits.charAt(i)).forEach(t -> tmp.add(tmpResult + t));
            }
            result = tmp;
        }

        return result;
    }
}