def merge(nums1, m, nums2, n) -> None: # O(m+n))
    i,j,k = 0,0,0 # O(1)
    A = [0 for _ in range(n+m)] # O(m+n)

    while i < m and j < n: # O(m+n)
        if nums1[i] <= nums2[j]: # O(1)
            A[k] = nums1[i] # O(1)
            i+=1 # O(1)
            k+=1 # O(1)
        else: # O(1)
            A[k] = nums2[j] # O(1)
            j+=1 # O(1)
            k+=1 # O(1)
    
    if i >= m: # O(1)
        A[k:] = nums2[j:n] # O(n)
    else: # O(1)
        A[k:] = nums1[i:m] # O(m)
    
    nums1[:] = A[:] # O(m+n)
    print(nums1) # O(m+n)

# ======================================================================

nums1 = [2,0]
m, n = 1, 1
nums2 = [1]

merge(nums1, m, nums2, n)