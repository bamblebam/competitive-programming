import collections


class Solution:
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        for word in strs:
            vector = [0]*26
            for letter in word:
                vector[ord(letter)-ord('a')] += 1
            anagrams[tuple(vector)].append(word)
        return anagrams.values()
