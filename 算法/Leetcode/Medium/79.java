/**
 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



 示例:

 board =
 [
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
 ]

 给定 word = "ABCCED", 返回 true
 给定 word = "SEE", 返回 true
 给定 word = "ABCB", 返回 false


 提示：

 board 和 word 中只包含大写和小写英文字母。
 1 <= board.length <= 200
 1 <= board[i].length <= 200
 1 <= word.length <= 10^3
 */

import java.util.*;
import java.util.stream.*;


class Solution {
    public boolean exist(char[][] board, String word) {
        int xLength = board[0].length;
        int yLength = board.length;
        boolean[][] isVisited = new boolean[yLength][xLength];
        for (int i = 0; i < yLength; i++) {
            for (int j = 0; j < xLength; j++) {
                boolean isFind = dfs(board, isVisited, word, 0, i, j);
                if (isFind) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(char[][] board, boolean[][] isVisited, String word, int wordIndex, int x, int y) {
        if (board[x][y] != word.charAt(wordIndex)) {
            return false;
        } else if (word.length() - 1 == wordIndex && board[x][y] == word.charAt(wordIndex)) {
            return true;
        }
        isVisited[x][y] = true;
        // 定义上下左右方向
        boolean result = false;
        int[][] directions = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        for (int[] action : directions) {
            int nextX = x + action[0];
            int nextY = y + action[1];
            if (nextX >= 0 && nextY >= 0 && nextX < board.length && nextY < board[0].length && !isVisited[nextX][nextY]) {
                boolean isFind = dfs(board, isVisited, word, wordIndex + 1, nextX, nextY);
                if (isFind) {
                    result = true;
                    break;
                }
            }
        }
        isVisited[x][y] = false;
        return result;
    }
}

