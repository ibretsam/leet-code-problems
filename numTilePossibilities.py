"""
1079. Letter Tile Possibilities
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

 

Constraints:
    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.
"""
from collections import Counter
def numTilePossibilities(tiles: str) -> int:
    """
    Time complexity: O(2^N)
    Space complexity: O(N)
    """
    count = Counter(tiles)
    def dfs():
        possible_sequences = 0
        for k, v in count.items():
            if v == 0:
                continue
            count[k] -= 1
            possible_sequences += 1 + dfs()
            count[k] += 1
        return possible_sequences
    return dfs()

def numTilePossibilities(tiles: str) -> int:
    """	
    Time complexity: O(2^N)
    Space complexity: O(N)
    """
    sequences = set()

    def backtrack(current, remaining):
        if current:
            sequences.add(current)
        
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i - 1]:
                continue
            backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])

    tiles = ''.join(sorted(tiles))
    backtrack('', tiles)
    return len(sequences)

print(numTilePossibilities("AAB")) #8