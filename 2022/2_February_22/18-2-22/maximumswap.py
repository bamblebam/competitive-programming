class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        create an index map
        go through each digit if you find a greater digit which is after curr swap it
        make sure it is the last occurence of that digit and you go in decreasing order
        '''
        num=str(num)
        indices=defaultdict(list)
        for i,digit in enumerate(num):
            indices[digit].append(i)
        for i,digit in enumerate(num):
            for j in range(9,int(digit),-1):
                vals=indices[str(j)]
                idx=bisect_left(vals,i)
                if idx<len(vals):
                    num=list(num)
                    num[i],num[vals[-1]]=str(j),digit
                    return "".join(num)
        return num