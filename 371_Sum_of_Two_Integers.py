class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # only useful for none negative add
        """
        al = map(lambda x: int(x), str(bin(a)).split('b')[1])[::-1]
        bl = map(lambda x: int(x), str(bin(b)).split('b')[1])[::-1]
        cl = al[:] if len(al) > len(bl) else bl[:]
        add = 0
        for i in range(min(len(al), len(bl))):
            cl[i] = al[i] ^ bl[i] ^ add
            add = 1 if (al[i] & bl[i] or al[i] & add or bl[i] & add) else 0
        for j in range(min(len(al), len(bl)), len(cl)):
            t = cl[j]
            cl[j] ^= add
            if t & add:
                add = 1
            else:
                add = 0
                break
        r = reduce(lambda x, y: str(x) + str(y), cl, '')[::-1]
        r = str(add) + r if add else r
        return int(r, 2)
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


if __name__ == '__main__':
    print(Solution().getSum(-5, 4))
