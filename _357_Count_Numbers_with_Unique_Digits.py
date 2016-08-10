def cal(n):
    re = 1
    for i in range(n):
        re *= i + 1
    return re


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        re = 0
        re2 = 0
        for i in range(2, n+1):
            re += cal(n) / (cal(n-i) * cal(i))
            re2 += cal(n-1) / (cal(n-i) * cal(i-1))
        re2 -= n-1
        return pow(10, n) - re * 10 - re2

if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(3))
