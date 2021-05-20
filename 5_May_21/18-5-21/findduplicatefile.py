from collections import defaultdict


class Solution:
    def findDuplicate(self, paths):
        ans = defaultdict(list)
        for path in paths:
            dirs = path.split()
            for i in range(1, len(dirs)):
                name, content = dirs[i].split('(')
                ans[content[:-1]].append(f'{dirs[0]}/{name}')
        return [i for i in ans.values() if len(i) > 1]
