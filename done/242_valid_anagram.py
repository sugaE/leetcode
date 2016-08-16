class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        return sorted(s) == sorted(t)
        """
        return self.func(s) == self.func(t)

    @staticmethod
    def func(s):
        a = ord('a')
        r = map(lambda x: int(ord(x) - a), s)
        r.sort()
        return r

if __name__ == '__main__':
    print(Solution().isAnagram('anagram', 'nagaram'))
    print(Solution().isAnagram('rat', 'car'))
