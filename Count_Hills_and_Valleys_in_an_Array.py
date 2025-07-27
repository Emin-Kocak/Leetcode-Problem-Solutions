class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        clean = [nums[0]]

        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                clean.append(nums[i])

        count = 0
        for i in range(1, len(clean) - 1):
            if (clean[i] > clean[i - 1] and clean[i] > clean[i + 1]) or (clean[i] < clean[i - 1] and clean[i] < clean[i + 1]):
                count += 1
        return count