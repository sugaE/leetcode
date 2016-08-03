class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return map(lambda i: str(bin(i)).count('1'), range(num + 1))

if __name__ == '__main__':
    print(Solution().countBits(0))
