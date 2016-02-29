class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # total = reduce(lambda x, y: x+y, map(lambda x: int(x), str(num)))
        # return total if total < 10 else self.addDigits(total)

        return num % 9
