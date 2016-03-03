class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int

        sum([26**i*(string.uppercase.index(c)+1) for (c,i) in zip(s[::-1],range(0,len(s)))])
        """
        # A to Z total 26
        s = s.upper()
        r = 0
        for n in s:
            r = r * 26 + ord(n) - ord('A') + 1
        # print(r)
        return r

if __name__ == '__main__':
    Solution().titleToNumber('A')
    Solution().titleToNumber('BA')
    Solution().titleToNumber('DBA')
