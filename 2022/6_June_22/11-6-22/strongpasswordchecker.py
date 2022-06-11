class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special_chars="!@#$%^&*()-+"
        n=len(password)
        
        if n<8:
            return False
        
        upper=0
        lower=0
        digit=0
        specs=0
        for c in password:
            if c.isupper():
                upper+=1
            elif c.islower():
                lower+=1
            elif c.isdigit():
                digit+=1
            elif c in special_chars:
                specs+=1
                
        if upper==0 or lower==0 or digit==0 or specs==0:
            return False
        
        for i in range(1,n):
            if password[i-1]==password[i]:
                return False
        
        return True