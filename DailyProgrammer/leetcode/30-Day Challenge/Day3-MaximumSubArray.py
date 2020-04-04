'''
Problem: Given an integer array nums, find the contiguous subarray (containing 
at least one number) which has the largest sum and return its sum.   
'''
def maxSubArray(self, nums: List[int]) -> int:
    
        sumMax = nums[0] 
        realMax = nums[0] 
        for i in range(1,len(nums)): 
            realMax = max(nums[i], realMax + nums[i]) 
            sumMax = max(sumMax,realMax) 
            
        return sumMax