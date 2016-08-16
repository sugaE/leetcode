#!/usr/bin/env python
# coding:utf-8


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        为什么这群人位运算都算的这么好！
        x= reduce(lambda i,j: i^j, nums)
        n1 = reduce(lambda i,j: i^j if j & x & -x else i^0, nums, 0)
        return [x^n1, n1]
        """
        nums.sort()
        if len(nums) < 3:
            return nums
        j = 0
        # for i in range(0, l, step):
        while j+1 < len(nums):
            if not nums[j+1] > nums[j]:
                nums.pop(j)
                nums.pop(j)
            else:
                j += 1
        return nums

if __name__ == '__main__':
    # print(Solution().singleNumber([0,1,1,2]))
    print(Solution().singleNumber([0,1,1,2,2,4,6,4]))
