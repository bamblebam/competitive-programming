class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        pairs=list()
        
        for spell in spells:
            target=math.ceil(success/spell)
            idx=bisect_left(potions,target)
            if idx>=n:
                pairs.append(0)
            else:
                pairs.append(n-idx)
        
        return pairs