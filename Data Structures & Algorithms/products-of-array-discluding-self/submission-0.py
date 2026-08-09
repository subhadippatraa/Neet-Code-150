class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums)
        left=1
        n=len(nums)
        for i,num in enumerate(nums):
            ans[i]=left
            left*=num
        right=1

        for i in range(n-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans

        

        