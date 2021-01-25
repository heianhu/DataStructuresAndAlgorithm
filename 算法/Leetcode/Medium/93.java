/**
 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。



 示例 1：

 输入：s = "25525511135"
 输出：["255.255.11.135","255.255.111.35"]
 示例 2：

 输入：s = "0000"
 输出：["0.0.0.0"]
 示例 3：

 输入：s = "1111"
 输出：["1.1.1.1"]
 示例 4：

 输入：s = "010010"
 输出：["0.10.0.10","0.100.1.0"]
 示例 5：

 输入：s = "101023"
 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


 提示：

 0 <= s.length <= 3000
 s 仅由数字组成
 */

import java.util.*;


class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if (s.length() > 12 || s.length() < 4) {
            return result;
        }
        List<String> resultTmp = new ArrayList<>();
        resultTmp.add("");
        dfs(result, resultTmp, s, 0);
        return result;
    }

    void dfs(List<String> result, List<String> resultTmp, String str, int index) {
        if (resultTmp.size() > 4 ||
                (resultTmp.get(resultTmp.size() - 1).length() > 0 && Integer.parseInt(resultTmp.get(resultTmp.size() - 1)) > 255) ||
                (resultTmp.get(resultTmp.size() - 1).length() > 0 && !resultTmp.get(resultTmp.size() - 1).equals(String.valueOf(Integer.parseInt(resultTmp.get(resultTmp.size() - 1)))))) {
            return;
        }
        if (index == str.length()) {
            if (resultTmp.size() == 4) {
                result.add(String.join(".", resultTmp));
            }
            return;
        }
        // 继续使用当前数字
        if (resultTmp.get(resultTmp.size() - 1).length() < 3) {
            resultTmp.set(resultTmp.size() - 1, resultTmp.get(resultTmp.size() - 1) + str.charAt(index));
            dfs(result, resultTmp, str, index + 1);
            resultTmp.set(resultTmp.size() - 1, resultTmp.get(resultTmp.size() - 1).substring(0, resultTmp.get(resultTmp.size() - 1).length() - 1));
        }

        // 将当前数字作为新的一段
        if (resultTmp.size() < 4 && !resultTmp.get(resultTmp.size() - 1).equals("")) {
            resultTmp.add(String.valueOf(str.charAt(index)));
            dfs(result, resultTmp, str, index + 1);
            resultTmp.remove(resultTmp.size() - 1);
        }

    }
}

