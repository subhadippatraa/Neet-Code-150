class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp={}
        max_count=0
        for i,num in enumerate(nums):
            mapp[num]=i
        
        for key,values in mapp.items():
            count=0
            if key+1 not in mapp:
                while key in mapp:
                    count+=1
                    key-=1
            max_count=max(max_count,count)
        return max_count
            