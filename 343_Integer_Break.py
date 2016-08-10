class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1
        y, l = divmod(n, 3)
        left = {0: lambda x: pow(3, x), 1: lambda x: pow(3, x-1) * 4, 2: lambda x: pow(3, x) * 2}
        return left.get(l)(y)


if __name__ == '__main__':
    print(Solution().integerBreak(2))
