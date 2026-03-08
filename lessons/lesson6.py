from typing import List


'''     n1  n2
         |   |
   i = 0 1 2 3
nums = 8 2 9 7

loop 0 1 2: # 2
    loop 1 2 3:
        sum = 2 + 3

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j 

res = Solution().twoSum(nums=[2,13,15,7],target=9)
print(res)

#     01234
# ex = 'hello'
# for i in range(len(ex)): # 5 0-4
#     e = ex[i]
#     print(e,i)
#     ...