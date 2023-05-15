def jump(nums):
    reach = 0
    n = len(nums)
    i = 0
    count = 0

    while reach < n-1:
        for j in range(i, reach+1):
            reach = max(j+nums[j], reach)
            i = j+1
        count += 1
    return count

nums = [2,3,1,1,4]
jump(nums)