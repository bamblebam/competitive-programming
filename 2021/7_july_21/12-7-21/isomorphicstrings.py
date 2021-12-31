from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {k: v for k, v in sorted(
            Counter(s).items(), key=lambda item: item[1], reverse=True)}
        s2 = {k: v for k, v in sorted(
            Counter(t).items(), key=lambda item: item[1], reverse=True)}
        char_map = dict()
        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False
        s1k, s2k = list(s1.keys()), list(s2.keys())
        for i in range(n1):
            if s1[s1k[i]] == s2[s2k[i]]:
                char_map[s1k[i]] = s2k[i]
            else:
                return False
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if char_map[c1] != c2:
                return False
        return True
