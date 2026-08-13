class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums=sorted(nums)
        n=len(nums)
        ans=[]
        for i,num in enumerate(sorted_nums):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                continue
            j=i+1
            k=n-1
            #
            while j<k:
                summ=sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
                if summ==0:
                    ans.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j+=1
                    k-=1
                    while j<k and sorted_nums[j]==sorted_nums[j-1]:
                        j+=1
                    while j<k and sorted_nums[k]==sorted_nums[k+1]:
                        k-=1
                elif summ>0:
                    k-=1
                else:
                    j+=1

        return ans


