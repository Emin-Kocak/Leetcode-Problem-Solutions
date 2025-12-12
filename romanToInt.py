class Solution(object):
    def romanToInt(self, s):
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0 

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: romans[x],s))
    
# other possible solution

        for i in range(len(s-1)):
            if romans[s[i]] < romans[s[i+1]]:
                ans -= romans[s[i]]
            else:
                ans += romans[s[i]]
        return ans + romans[s[-1]]





    # Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))      # Output: 3
    print(solution.romanToInt("IV"))       # Output: 4
    print(solution.romanToInt("IX"))       # Output: 9
    print(solution.romanToInt("LVIII"))    # Output: 58
    print(solution.romanToInt("MCMXCIV"))  # Output: 1994