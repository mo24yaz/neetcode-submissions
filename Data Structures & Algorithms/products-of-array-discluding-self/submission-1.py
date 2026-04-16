# Brute Force Solution (O(n^2))
def productExceptSelf_bruteforce(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        num = 1
        for j in range(len(nums)):
            if i != j:
                num = num * nums[j]
        res.append(num)

    return res

# Optimized Solution (O(n))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = 1
        right = 1
        
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

