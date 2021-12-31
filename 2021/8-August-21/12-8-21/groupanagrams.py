from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        word_map = defaultdict(list)
        for word in strs:
            vector = [0]*26
            for letter in word:
                vector[ord(letter)-ord('a')] += 1
            word_map[tuple(vector)].append(word)
        return word_map.values()
