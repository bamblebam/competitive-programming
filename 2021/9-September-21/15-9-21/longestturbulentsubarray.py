class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        temp=0
        for k in range(n-1):
            if (k%2 and arr[k]>arr[k+1]) or (not k%2 and arr[k]<arr[k+1]):
                temp+=1
            else:
                ans=max(temp,ans)
                temp=0
        ans=max(temp,ans)
        temp=0
        for k in range(n-1):
            if (k%2 and arr[k]<arr[k+1]) or (not k%2 and arr[k]>arr[k+1]):
                temp+=1
            else:
                ans=max(temp,ans)
                temp=0
        ans=max(temp,ans)
        return ans+1