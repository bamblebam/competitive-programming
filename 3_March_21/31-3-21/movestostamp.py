class Solution:
    def movesToStamp(self, stamp, target):
        if stamp == target:
            return [0]
        stamp, target = list(stamp), list(target)
        stamp_len, target_len = len(stamp), len(target)-len(stamp)+1
        stamp_diff, target_diff = True, True
        answer = list()
        while(target_diff):
            target_diff = False
            for i in range(target_len):
                stamp_diff = False
                for j in range(stamp_len):
                    if target[i+j] == '*':
                        continue
                    elif target[i+j] != stamp[j]:
                        break
                    else:
                        stamp_diff = True
                else:
                    if stamp_diff:
                        target_diff = True
                        for k in range(i, i+stamp_len):
                            target[k] = "*"
                        answer.append(i)
        for letter in target:
            if letter is not "*":
                return []
        return reversed(answer)
