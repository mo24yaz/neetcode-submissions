# Brute Force Solution (O(n^2))
def hasDuplicate_bruteforce(self, nums: List[int]) -> bool:
    res = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                res = True

    return res


# Optimized Solution (O(n))
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False