class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [dict() for _ in range(4*self.n)]

        def build(start, end, idx):
            self.tree[idx]['left'] = start
            self.tree[idx]['right'] = end
            if start == end:
                self.tree[idx]['val'] = nums[start]
                return
            mid = (start+end)//2
            build(start, mid, 2*idx)
            build(mid+1, end, 2*idx+1)
            self.tree[idx]['val'] = self.tree[2*idx]['val'] + \
                self.tree[2*idx+1]['val']

        build(0, self.n-1, 1)

    def update(self, index: int, val: int) -> None:

        def update_tree(pos, val, idx):
            i, j = self.tree[idx]['left'], self.tree[idx]['right']
            if i == j and i == pos:
                self.tree[idx]['val'] = val
                return
            mid = (i+j)//2
            if pos <= mid:
                update_tree(pos, val, 2*idx)
            else:
                update_tree(pos, val, 2*idx+1)
            self.tree[idx]['val'] = self.tree[2*idx]['val'] + \
                self.tree[2*idx+1]['val']

        update_tree(index, val, 1)

    def sumRange(self, left: int, right: int) -> int:

        def query(left, right, idx):
            i, j = self.tree[idx]['left'], self.tree[idx]['right']
            if i == left and j == right:
                return self.tree[idx]['val']
            mid = (i+j)//2
            if i <= left and right <= mid:
                return query(left, right, 2*idx)
            if mid+1 <= left and right <= j:
                return query(left, right, 2*idx+1)
            return query(left, mid, 2*idx)+query(mid+1, right, 2*idx+1)

        return query(left, right, 1)
