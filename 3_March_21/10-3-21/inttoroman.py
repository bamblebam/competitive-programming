class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ["I", "IV", "V", "IX", "X", "XL",
                 "L", "XC", "C", "CD", "D", "CM", "M"]
        integers = [1, 4, 5, 9, 10, 40, 50, 90,
                    100, 400, 500, 900, 1000]
        answer = ""
        i = 12
        while num:
            div = num//integers[i]
            num %= integers[i]
            while div:
                answer += roman[i]
                div -= 1
            i -= 1
        return answer


sol = Solution()
print(sol.intToRoman(3549))
