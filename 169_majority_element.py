class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in set(nums):
            if nums.count(n) > int(len(nums)/2):
                return n

if __name__ == '__main__':
    # print(Solution().majorityElement([1,2.3]))
    print(Solution().majorityElement([3,2,3]))
