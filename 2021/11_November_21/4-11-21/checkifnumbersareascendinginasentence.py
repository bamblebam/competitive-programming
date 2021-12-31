class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        #split the string and iterate over each word.
        #if digit check if it is greater and then update
        prev=-1
        for token in s.split(' '):
            if token.isdigit():
                curr=int(token)
                if curr<=prev:
                    return False
                prev=curr
        return True
        