class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for x in emails:
            local, domain = x.split('@')
            new = ''
            for letter in local:
                if letter == '.':
                    continue
                elif letter == '+':
                    break
                else:
                    new += letter
            ans.add('@'.join([new, domain]))
        return len(ans)
