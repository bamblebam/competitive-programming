class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        pairs={")":"(","}":"{","]":"["}
        for x in s:
            if not stack:
                stack.append(x)
            else:
                if x in pairs.keys():
                    if stack[-1]==pairs[x]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(x)
        return len(stack)==0