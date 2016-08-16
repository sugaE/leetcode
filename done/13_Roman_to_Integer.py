
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        for i in s:
            l.append(d[i.upper()])
        return self.reduc(l)

    def reduc(self, l):
        i = 1
        flag = True
        while i < len(l):
            x, y = l[i - 1], l[i]
            if x < y:  # IV
                y -= x
                l[i - 1], l[i] = 0, y
                l.remove(0)
                flag = False
            i += 1
        if flag:
            return sum(l)
        else:
            return self.reduc(l)


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCVI"))  # 1996 from 1-I to 3999-IMMMM.
