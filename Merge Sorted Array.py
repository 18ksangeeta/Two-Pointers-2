class Solution:
    # leetcode URL : https://leetcode.com/problems/merge-sorted-array/
    # Problem : 88. Merge Sorted Array
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s_nums1 = m-1
        s_nums2 = n-1
        insert_pos = m+n-1
        
        while s_nums2>=0 and s_nums1>=0:
            if nums2[s_nums2] > nums1[s_nums1]:
                nums1[insert_pos] = nums2[s_nums2] 
                s_nums2 = s_nums2-1
            else:
                nums1[insert_pos] = nums1[s_nums1]
                s_nums1 = s_nums1-1
            insert_pos = insert_pos-1
                
        if s_nums2>0:
            while s_nums2>=0:
                nums1[insert_pos] = nums2[s_nums2]
                s_nums2 = s_nums2-1
                insert_pos = insert_pos-1
        