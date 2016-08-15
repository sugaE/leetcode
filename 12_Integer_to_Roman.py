
d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n, m = divmod(num, 1000)
        l1 = n * 'M'
        l2, m = self.cal(m, 100)
        l3, m = self.cal(m, 10)
        l4, m = self.cal(m, 1)
        return l1 + l2 + l3 + l4

    def cal(self, m, base):
        n, m = divmod(m, base)
        li = n * [base]
        l = len(li)
        if l == 4:
            li = d[base] + d[base * 5]
        elif 4 < l < 9:
            li = li[5:]
            li = d[base * 5] + len(li) * d[base]
        elif l == 9:
            li = d[base] + d[base * 10]
        return li, m


if __name__ == '__main__':
    print(Solution().intToRoman(2996))  # MCMXCVI  # from 1 to 3999.
