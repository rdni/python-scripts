class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        if all([merged[0] == merged[i] for i in range(len(merged))]):
            return merged[0]
        if len(merged) % 2 != 0:
            return float(merged[int((len(merged)/2)+0.5)])
        else:
            n1 = merged[int(len(merged)/2)]
            n2 = merged[int((len(merged)/2)-1)]
            return float(float(n1+n2)/2)
        
s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))