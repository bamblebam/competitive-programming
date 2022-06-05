class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words=list(sentence.split(" "))
        for i,word in enumerate(words):
            if len(word)<2 or not "$"==word[0] or not word.count("$")==1:
                continue
            if not word[1:].isnumeric():
                continue
            price=round(int(word[1:])*(1 - discount/100),2)
            words[i]="$%.2f"%price
        return " ".join(words)
            