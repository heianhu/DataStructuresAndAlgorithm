/**
 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

 示例 1:

 输入: num1 = "2", num2 = "3"
 输出: "6"
 示例 2:

 输入: num1 = "123", num2 = "456"
 输出: "56088"
 说明：

 num1 和 num2 的长度小于110。
 num1 和 num2 只包含数字 0-9。
 num1 和 num2 均不以零开头，除非是数字 0 本身。
 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 */

import java.util.*;


class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        int num1Length = num1.length();
        int num2Length = num2.length();
        int[] resultList = new int[num1Length + num2Length];
        for (int i = num1Length - 1; i >= 0; i--) {
            int num1IndexNum = num1.charAt(i) - '0';
            for (int j = num2Length - 1; j >= 0; j--) {
                int num2IndexNum = num2.charAt(j) - '0';
                resultList[i + j + 1] += num1IndexNum * num2IndexNum;
            }
        }
        for (int i = num1Length + num2Length - 1; i > 0; i--) {
            resultList[i - 1] += resultList[i] / 10;
            resultList[i] %= 10;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < num1Length + num2Length; i++) {
            if (i == 0 && resultList[i] == 0) {
                continue;
            }
            result.append(resultList[i]);
        }
        return result.toString();
    }
}

