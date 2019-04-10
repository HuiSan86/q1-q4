# Q1
nums = [1,2,3,4]

def sum_Func(nums):
    return [sum(nums) - item for item in nums]

print (sum_Func(nums))