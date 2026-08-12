class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor
