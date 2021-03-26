import collections


class Solution:
    def wordSubsets(self, A, B):
        answers = list()
        count2 = [0]*26
        for word in B:
            count3 = collections.Counter(word)
            for key, item in count3.items():
                count2[ord(key)-ord('a')] = max(item,
                                                count2[ord(key)-ord('a')])
        for word in A:
            count = [0]*26
            count4 = collections.Counter(word)
            for key, item in count4.items():
                count[ord(key)-ord('a')] = max(item,
                                               count[ord(key)-ord('a')])
            if all(x >= y for x, y in zip(count, count2)):
                answers.append(word)
        return answers


sol = Solution()
print(sol.wordSubsets(A=["amazon", "apple", "facebook",
      "google", "leetcode"], B=["ec", "oc", "ceo"]))
