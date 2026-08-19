class Solution:
    def helper(self,index,nums,ans,temp):
        if(index>=len(nums)):
            ans.append(nums.copy())
            return
        
        for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            self.helper(index+1,nums,ans,temp)
            nums[i],nums[index]=nums[index],nums[i]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        self.helper(0,nums,ans,temp)
        return ans