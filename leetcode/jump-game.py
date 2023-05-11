'''
    I could not solve this problem. Had to look up solutions.   
'''

def canJump(nums):
    n = len(nums)
    reach = 0

    for i in range(n):
        if reach < i: return False
        reach = max(reach, i+nums[i])
        if reach >= n-1: return True


# I like this solution
def canJump(nums):

    goal=len(nums)-1

    for i in range(len(nums)-2,-1,-1):
        if i + nums[i] >=goal:
            goal=i
        
    return goal==0