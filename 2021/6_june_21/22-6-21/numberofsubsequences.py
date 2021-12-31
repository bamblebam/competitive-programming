from collections import defaultdict
from bisect import bisect_right


class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        ans = 0
        idx_map = defaultdict(list)
        for i, v in enumerate(s):
            idx_map[v].append(i)

        def is_subsequence(word):
            curr = -1
            for letter in word:
                if idx_map[letter]:
                    pos = bisect_right(idx_map[letter], curr)
                    if pos == len(idx_map[letter]):
                        return False
                    curr = idx_map[letter][pos]
                else:
                    return False
            return True

        for word in words:
            if is_subsequence(word):
                ans += 1

        return ans
