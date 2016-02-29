class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        return reduce(lambda a,b:a^b, nums)
        """
        nums.sort()
        if len(nums) < 2:
            return nums[0]
        for i in range(0, len(nums)-2, 2):
            if nums[i+1] > nums[i]:
                return nums[i]
        return nums[len(nums)-1]
