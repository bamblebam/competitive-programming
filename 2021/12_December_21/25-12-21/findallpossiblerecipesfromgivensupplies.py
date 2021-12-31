class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        e=defaultdict(list)
        n=len(recipes)
        prerequisites=[0]*n
        for i in range(n):
            x=recipes[i]
            y=ingredients[i]
            for u in y:
                e[u].append(i)
                prerequisites[i]+=1
        queue=deque(supplies)
        ans=list()
        while queue:
            supply=queue.popleft()
            for r in e[supply]:
                prerequisites[r]-=1
                if prerequisites[r]==0:
                    ans.append(recipes[r])
                    queue.append(recipes[r])
        return ans