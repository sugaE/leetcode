class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums):
        #     return False
        # for n in nums:
        #     if nums.count(n)>1:
        #         return False
        # return True
        return len(nums) > len(set(nums))

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2.3]))
    print(Solution().containsDuplicate([1,2.3,2]))
