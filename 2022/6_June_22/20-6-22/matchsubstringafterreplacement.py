class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        """
        just use brute force and go over all the possible substrings and check if they match
        """
        mapping_dict=defaultdict(set)
        for old,new in mappings:
            mapping_dict[old].add(new)
        
        m,n=len(sub),len(s)
        for i in range(n-m+1):
            flag=True
            for s_val,sub_val in zip(s[i:i+m],sub):
                if s_val==sub_val or s_val in mapping_dict[sub_val]:
                    continue
                else:
                    flag=False
                    break
            if flag:
                return True
        
        return False
