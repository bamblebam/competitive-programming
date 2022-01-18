# Nice and clean solution, upvoted. Let me try to explain this most important line of code:

# if i+1 < len(batteries) and batteries[i+1]*(i+1) - prefix > extra: return (prefix + extra) // (i+1)
# This line maps to the explanation:

# Give extra reservoir to the first i (zero-indexed) batteries and check if they can last as much as the battery at index (i+1), return (lowest + 2nd lowest + ... + extra)//(i+1);

# Why ? Because if, with the extra reservoir, the previous ones still cannot last averagely as much as the current battery, they will die and cannot fulfill the requirement of n running computers. So we can return

# (prefix sum + extra)/(prefix batteries count) ==> (prefix + extra) // (i+1).
# Then you may ask, how to understand below comparison ?

# batteries[i+1]*(i+1) - prefix > extra
# If we just move the prefix to right side of the inequality

# batteries[i+1]*(i+1) > extra + prefix
# And make the multiply into division

# batteries[i+1] > (extra + prefix)//(i+1)
# The semantics is clear now, isn't it? It just says

# with the extra reservoir, the previous ones still cannot last averagely as much as the current battery!

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        #the batteries can be considered as n biggest batteries + sum of all the other batteries as 1
        #then we go over the n batteries and check if that particular battery has more capacity than all the previous batteries + extra
        #if yes the max we can run for is the extra + prev batteries divided by total computers traversed so far
        #if entire n batteries are travelled we just add all batteries and divide them by computers
        #this works because for batteries that are bigger than extra + prev will make sure that that number of computers will run the mose
        #we only need to check for the remaining computers
        batteries.sort()
        extra=sum(batteries[:-n])
        batteryPack=batteries[-n:]
        
        ans=0
        prefix=0
        for i,x in enumerate(batteryPack):
            prefix+=x
            if i+1<len(batteryPack) and batteryPack[i+1]>(extra+prefix)/(i+1):
                return (extra+prefix)//(i+1)
        return (extra+prefix)//n