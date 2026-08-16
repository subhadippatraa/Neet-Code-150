class Solution:
    def helper(self, nums, idx, target, temp, ans):
        if target == 0:
            ans.append(temp.copy())
            return

        if idx >= len(nums):
            return

        if nums[idx] <= target:
            temp.append(nums[idx])
            self.helper(nums, idx, target - nums[idx], temp, ans)
            temp.pop()
        self.helper(nums, idx + 1, target, temp, ans)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.helper(nums, 0, target, temp, ans)

        return ans