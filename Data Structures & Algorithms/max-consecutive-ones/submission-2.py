class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                out = max(out, count)
            else:
                count = 0
        return out