class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''-1:off,1:on'''
        # bulbs = [-1] * n
        # for i in range(0, len(bulbs)):
        #     for j in range(i, len(bulbs), i+1):
        #         bulbs[j] = -bulbs[j]
        # return bulbs.count(1)
        return int(n ** 0.5)


if __name__ == '__main__':
    print(Solution().bulbSwitch(999999))
