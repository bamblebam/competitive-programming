class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=list()
        n=len(arr)
        best=float("inf")
        for i in range(1,n):
            x=arr[i]-arr[i-1]
            if x<best:
                ans=[[arr[i-1],arr[i]]] 
                best=x
            elif x==best:
                ans.append([arr[i-1],arr[i]])
            else:
                continue
        return ans