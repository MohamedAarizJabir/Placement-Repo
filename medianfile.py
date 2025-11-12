def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    
   
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m

    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i
        
        maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
        minRight1 = float('inf') if i == m else nums1[i]
        
        maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
        minRight2 = float('inf') if j == n else nums2[j]
        
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
           
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            high = i - 1
        else:
            low = i + 1
