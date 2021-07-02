from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        n = len(arr)
        idx = bisect_left(arr, x)
        left = idx-1 if idx > 0 else -1
        right = idx if idx < n else n
        ans = list()
        while len(ans) < k:
            left_el = arr[left]
            right_el = arr[right] if right < n else 0
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= n:
                ans.append(arr[left])
                left -= 1
            elif abs(x-left_el) < abs(x-right_el):
                ans.append(arr[left])
                left -= 1
            elif abs(x-right_el) < abs(x-left_el):
                ans.append(arr[right])
                right += 1
            else:
                if arr[left] < arr[right]:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
        return sorted(ans)
