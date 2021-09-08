class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locks = [0]*len(parent)
        self.children = defaultdict(list)
        for i, node in enumerate(parent):
            self.children[node].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0:
            self.locks[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # check if node is unlocked
        flag1 = True
        if self.locks[num] != 0:
            flag1 = False

        # check if atleast one descendant is locked
        flag2 = False

        def check_locked(node):
            nonlocal flag2
            if self.locks[node] != 0:
                # print(node)
                flag2 = True
                return
            for child in self.children[node]:
                check_locked(child)
        check_locked(num)

        # check if all ancestors are unlocked
        flag3 = True

        def check_unlocked(node):
            nonlocal flag3
            if self.locks[node] != 0:
                flag3 = False
                return
            if self.parent[node] != -1:
                check_unlocked(self.parent[node])
        check_unlocked(num)

        # unlocking all descendent nodes if upgradable
        def unlock_descendants(node):
            self.locks[node] = 0
            for child in self.children[node]:
                unlock_descendants(child)
        if all([flag1, flag2, flag3]):
            unlock_descendants(num)
            self.locks[num] = user
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
