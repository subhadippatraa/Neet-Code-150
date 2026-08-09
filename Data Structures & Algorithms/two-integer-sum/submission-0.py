class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp={}

        for i,num in enumerate(nums):
            res=target-num
            if res in mapp:
                return [mapp[res],i]
            mapp[num]=i
        return [-1,-1]