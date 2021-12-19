class Solution:
    def decodeString(self, s: str) -> str:
        #use stack
        #if open bracket push the number and empty string
        #if close bracket pop the string to be multiplied, num and the prev string add them and put it back in the stack
        #if normal letters just add it to the last stack entry
        #can also be done using recursion
        idx,num,stack=0,0,[""]
        while idx<len(s):
            if s[idx].isdigit():
                num=num*10+int(s[idx])
            elif s[idx]=="[":
                stack.append(num)
                stack.append("")
                num=0
            elif s[idx]=="]":
                s1=stack.pop()
                rep=stack.pop()
                s2=stack.pop()
                stack.append(s2+s1*rep)
            else:
                stack[-1]+=s[idx]
            idx+=1
        return "".join(stack)
            