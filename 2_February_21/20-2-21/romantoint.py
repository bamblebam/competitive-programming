import collections


class Solution:
    def romanToInt(self, s):
        integers = collections.defaultdict(None)
        integers.update({'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000, "N": 0})
        sum_ = 0
        char_count = 1
        lastchar = "N"
        for char in s:
            if lastchar == char:
                char_count += 1
                lastchar = char
                sum_ += integers[char]
            elif lastchar != char and integers[lastchar] > integers[char]:
                char_count = 1
                lastchar = char
                sum_ += integers[char]
            elif integers[lastchar] < integers[char]:
                sum_ -= integers[lastchar]*char_count*2
                sum_ += integers[char]
                lastchar = char
                char_count = 1
            else:
                print("bam")
        return sum_


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
