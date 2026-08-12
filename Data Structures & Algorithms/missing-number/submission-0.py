class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor_of_n_numbers=0
        xor_of_nums=0

        for i in range(len(nums)+1):
            xor_of_n_numbers^=i
        for num in nums:
            xor_of_nums^=num
        return xor_of_n_numbers^xor_of_nums