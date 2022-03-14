class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=list()
        path=path.split("/")
        for dir in path:
            if dir in [" ","","."]:
                continue
            if dir in [".."]:
                if stack:
                    stack.pop()
                continue
            stack.append(dir)
        return "/" + "/".join(stack)