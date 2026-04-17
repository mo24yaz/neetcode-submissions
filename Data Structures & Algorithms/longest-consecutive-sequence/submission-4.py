class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        curr_streak = 1
        max_streak = 1

        for i in range(1, len(nums)):
            
            if nums[i-1] == nums[i]:
                continue

            elif nums[i-1] + 1 == nums[i]:
                curr_streak += 1

            else:
                max_streak = max(max_streak, curr_streak)
                curr_streak = 1

        max_streak = max(max_streak, curr_streak)

        return max_streak
        

        