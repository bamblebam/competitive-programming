from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_count = Counter(t)
        required = len(t_count)
        filtered_s = [(i, char) for i, char in enumerate(s) if char in t_count]
        l, r = 0, 0
        ans = float('inf'), None, None
        window_count = dict()
        formed = 0
        while r < len(filtered_s):
            end, char = filtered_s[r]
            window_count[char] = window_count.get(char, 0)+1
            if window_count[char] == t_count[char]:
                formed += 1
            while l <= r and formed == required:
                start, char = filtered_s[l]
                if end-start+1 < ans[0]:
                    ans = (end-start+1, start, end)
                window_count[char] -= 1
                if window_count[char] < t_count[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
