class Solution:
    def advantageCount(self, A, B):
        sorted_a = sorted(A)
        sorted_b = sorted(B)
        assigned = {b: [] for b in B}
        remaining = list()
        j = 0
        for a in sorted_a:
            if a > sorted_b[j]:
                assigned[sorted_b[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]
