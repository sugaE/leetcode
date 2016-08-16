class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = len(matrix)
        li = []
        for i in range(l):
            for j in range(l):
                li.append(matrix[i][j])
            if len(li) < k:
                continue
            li.sort()
            if li[k - 1] < min(matrix[i]):
                break
        return li[k - 1]


if __name__ == '__main__':
    print(Solution().kthSmallest([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 5))
