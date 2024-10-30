"""
212. Word Search II
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]], 
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['is_word'] = True

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    visited, res = set(), set()
    m, n = len(board), len(board[0])

    def backtrack(curr_res, i, j, node):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] not in node:
            return

        visited.add((i, j))
        node = node[board[i][j]]
        curr_res += board[i][j]
        if 'is_word' in node:
            res.add(curr_res)

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in direction:
            x, y = dx + i, dy + j
            backtrack(curr_res, x, y, node)

        visited.remove((i, j))

    for i in range(m):
        for j in range(n):
            backtrack("", i, j, trie.root)
    return list(res)

# Test cases
print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) # ["eat","oath"]
