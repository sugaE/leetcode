class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        # n = len(nums)
        # dp = [[0] * n for _ in xrange(n-1)]
        #
        # for k in xrange(2, n):
        #     for left in xrange(0, n - k):
        #         right = left + k
        #         for i in xrange(left + 1, right):
        #             dp[left][right] = max(dp[left][right],
        #               nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        #             print dp
        # return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().maxCoins([3,1,5,8,1]))
