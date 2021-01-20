/**
 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

 示例 1:

 输入:
 [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
 ]
 输出: [1,2,3,6,9,8,7,4,5]
 示例 2:

 输入:
 [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
 ]
 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int xLength = matrix[0].length;
        int yLength = matrix.length;
        int maxLength = Math.max(xLength, yLength);
        int usedIndex = 0;
        while (usedIndex <= maxLength / 2) {
            for (int i = usedIndex; i < xLength - usedIndex; i++) {
                result.add(matrix[usedIndex][i]);
            }
            if (usedIndex >= xLength - usedIndex) {
                break;
            }
            for (int i = usedIndex + 1; i < yLength - usedIndex; i++) {
                result.add(matrix[i][xLength - usedIndex - 1]);
            }
            if (usedIndex + 1 >= yLength - usedIndex) {
                break;
            }
            for (int i = xLength - usedIndex - 2; i >= usedIndex; i--) {
                result.add(matrix[yLength - usedIndex - 1][i]);
            }
            if (xLength - usedIndex - 2 < usedIndex) {
                break;
            }
            for (int i = yLength - usedIndex - 2; i >= usedIndex + 1; i--) {
                result.add(matrix[i][usedIndex]);
            }
            if (yLength - usedIndex - 2 < usedIndex + 1) {
                break;
            }
            usedIndex++;
        }
        return result;
    }
}

