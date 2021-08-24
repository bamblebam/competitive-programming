class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, img1 = num1.split('+')
        real2, img2 = num2.split('+')
        real = str(int(real1)*int(real2)+int(img1[:-1])*int(img2[:-1])*(-1))
        img = str(int(real1)*int(img2[:-1])+int(real2)*int(img1[:-1]))+'i'
        return '+'.join([real, img])
