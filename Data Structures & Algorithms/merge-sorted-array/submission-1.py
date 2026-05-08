class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort()
        nums2.sort()
        size=len(nums1)-m
        for i in range(size):
            nums1.remove(0)
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()