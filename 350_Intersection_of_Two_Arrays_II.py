class Solution(object):
    @staticmethod
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1).intersection(set(nums2))
        inter = []
        for i in s:
            inter.extend([i]*min(list(nums1).count(i), list(nums2).count(i)))
        return inter

if __name__ == '__main__':
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
