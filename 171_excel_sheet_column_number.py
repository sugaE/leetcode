class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A to Z total 26

        # return (len(s)-1) * 26 + ord(s.upper()[-1])-ord('A') + 1
        s = s.upper()
        r = 0
        for i in range(0, len(s)):
            r += (ord(s[i]) - ord('A') + 1) + r * 26
        print(r)
        return r


if __name__ == '__main__':
    Solution().titleToNumber('A')
    Solution().titleToNumber('BA')
    Solution().titleToNumber('DBA')
