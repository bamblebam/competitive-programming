class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n=len(parents)
        #make dict to store all children
        children=defaultdict(list)
        for i,parent in enumerate(parents):
            children[parent].append(i)
        
        best=-1
        bestn=0
        
        #find number of nodes in subtree and multiply it with the remaining nodes
        def helper(node):
            nonlocal best
            nonlocal bestn
            total=1
            product=1
            for child in children[node]:
                x=helper(child)
                product*=x
                total+=x
            if n-total>0:
                product*=n-total
            if product==best:
                bestn+=1
            if product>best:
                best=product
                bestn=1
            return total
        
        helper(0)
        return bestn
        