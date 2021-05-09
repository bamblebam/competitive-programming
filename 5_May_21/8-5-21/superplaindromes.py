import bisect


class Solution:
    answers = set()
    for i in range(1, 100000):
        even = int(str(i)+str(i)[::-1])**2
        odd = int(str(i)+str(i)[-2::-1])**2
        if str(even) == str(even)[::-1]:
            answers.add(even)
        if str(odd) == str(odd)[::-1]:
            answers.add(odd)
    answers = sorted(list(answers))

    def superpalindromesInRange(self, left: str, right: str) -> int:
        l, r = int(left), int(right)
        return bisect.bisect(self.answers, r)-bisect.bisect(self.answers, l-1)
