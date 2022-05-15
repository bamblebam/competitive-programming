class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        """
        sliding window: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/discuss/2038674/Python-Explanation-with-pictures-sliding-window
        
        binary search: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/discuss/2038177/Greedy-%2B-prefix-sum-%2B-binary-search-easy-to-understand-with-explanation
        """
        tiles.sort()
        n=len(tiles)
        prefix=[0]+list(accumulate(r-l+1 for l,r in tiles))
        j=0
        ans=0
        ends=[tile[1] for tile in tiles]
        
        for i,(l,_) in enumerate(tiles):
            r=min(ends[-1],carpetLen+l-1)
            while j<n and ends[j]<r:
                j+=1
            if tiles[j][0]>r: #the entire range is covered by carpet
                ans=max(ans,prefix[j]-prefix[i])
            else: #only part of the jth range is covered
                ans=max(ans,prefix[j+1]-prefix[i]-(ends[j]-r))
        
        return ans
            
                
            