class Solution:
    def calculate(self, s: str) -> int:
        #use 3 stacks
        #first stack to separate all nums and signs
        #second stack to perform * and / operations
        #third stack to perform + and - operations
        stack=list()
        s=s.replace(" ","")
        stack3=list()
        for i,x in enumerate(s):
            if not stack3:
                stack3.append(x)
                continue
            if x.isdigit():
                if stack3[-1].isdigit():
                    stack3[-1]+=x
                else:
                    stack3.append(x)
            else:
                stack3.append(x)
        print(stack3)
            
        for i,x in enumerate(stack3):
            if not stack:
                stack.append(x)
                continue
            if x.isdigit():
                if stack[-1]=="/":
                    stack.pop()
                    num1=int(stack.pop())
                    stack.append(str(num1//int(x)))
                elif stack[-1]=="*":
                    stack.pop()
                    num1=int(stack.pop())
                    stack.append(str(num1*int(x)))
                else:
                    stack.append(x)
            else:
                stack.append(x)

        stack2=list()
        for i,x in enumerate(stack):
            if not stack2:
                stack2.append(x)
                continue
            if x.isdigit():
                if stack2[-1]=="+":
                    stack2.pop()
                    num1=int(stack2.pop())
                    stack2.append(str(num1+int(x)))
                elif stack2[-1]=="-":
                    stack2.pop()
                    num1=int(stack2.pop())
                    stack2.append(str(num1-int(x)))
            else:
                stack2.append(x)
            
        s="".join(stack2)
        return int(s)
                