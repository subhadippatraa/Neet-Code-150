class Solution:
    def helper(self,nums,idx):
        if self.target==0:
            self.ans.append(self.temp.copy())
            return
        if(idx>=len(nums)):
            return
        if nums[idx]<=self.target:
            self.temp.append(nums[idx])
            self.target-=nums[idx]
            self.helper(nums,idx)
            self.temp.pop()
            self.target+=nums[idx]
        self.helper(nums,idx+1)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.target = target
        self.ans = []
        self.temp = []
        self.helper(nums,0)
        return self.ans
        