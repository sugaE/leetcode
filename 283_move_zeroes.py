class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 但leetcode不接受诶。python版本？
        l = len(nums)
        nums = filter(lambda x: x != 0, nums)
        nums.extend([0]*(l - len(nums)))
        print(nums)

if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])
