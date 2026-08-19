class Solution:
    def helper(self,nums,ans,temp,index):
        if(index>=len(nums)):
            ans.append(temp.copy())
            return
        temp.append(nums[index])
        self.helper(nums,ans,temp,index+1)
        temp.pop()
        self.helper(nums,ans,temp,index+1)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        self.helper(nums,ans,temp,0)
        return ans
        