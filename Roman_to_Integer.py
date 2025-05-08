class Solution(object):
    def romanToInt(self, s):
        symbols = {"I" : 1,"V": 5,"X":10,"L":50,"C":100,"D":500,"M":100}
        result = 0

        for index, i in enumerate(s):
            result += symbols[i]
            if index + 1 < len(s) and symbols[s[index + 1]] > symbols[s[index]]:
                result -= 2 *symbols[s[index]]#We multiplied by 2 because we already added the number we need to subtract above, so we need to subtract it twice
        
        return result

solution = Solution()
r = solution.romanToInt("IV")
print(r)