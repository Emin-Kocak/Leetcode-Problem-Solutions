class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        
        if not nums:
            return 0
        
        k = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1

# Example usage
solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))