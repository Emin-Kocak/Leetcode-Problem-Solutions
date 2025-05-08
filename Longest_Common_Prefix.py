class Solution(object):
    def longestCommonPrefix(self, strs):

        min_lenght = min(len(word) for word in strs)
        s  = ""
        for i in range((min_lenght)):
            current_char = strs[0][i]
            if all(word[i] == current_char for word in strs):
                s += current_char
            else: return s
        return s
    

solution = Solution()  # Solution sınıfından bir örnek oluşturuluyor
result = solution.longestCommonPrefix(strs=["flower", "flow", "flight"])
print(result)  