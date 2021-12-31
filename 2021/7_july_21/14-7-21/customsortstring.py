from collections import Counter


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        char_counts = Counter(str)
        order_chars = set(order)
        temp = list()
        for char in order:
            if char in char_counts:
                temp.append(char*char_counts[char])
        for char in char_counts:
            if char not in order_chars:
                temp.append(char*char_counts[char])
        return ''.join(temp)
