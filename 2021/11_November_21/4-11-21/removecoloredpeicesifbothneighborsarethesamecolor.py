class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        #put all indices of A and B who are in between 2 of the same kind in a dictionary
        #on their turns pop out the idx, if they cannot pop an idx they lose
        #instead of a dict with indices you can also use the count oof their occurrences
        idx_map=defaultdict(list)
        n=len(colors)
        for i in range(1,n-1):
            if colors[i-1]==colors[i]==colors[i+1]:
                idx_map[colors[i]].append(i)
        for i in range(1,n+1):
            if i%2:
                if idx_map['A']:
                    idx_map['A'].pop()
                else:
                    return False
            else:
                if idx_map['B']:
                    idx_map['B'].pop()
                else:
                    return True