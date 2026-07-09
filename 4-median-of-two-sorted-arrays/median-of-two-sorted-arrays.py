class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        nums1.extend(nums2)
        res=sorted(nums1)
        if len(res)%2==0:
            fn=res[(len(res)//2)-1]
            sn=res[(len(res)//2)]
            return (fn+sn)/2
        else:
            return res[len(res)//2]

        