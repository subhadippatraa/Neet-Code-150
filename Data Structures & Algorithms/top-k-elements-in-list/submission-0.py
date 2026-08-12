class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        ans = []
        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1

        sorted_map = sorted(mapp.items(), key=lambda x: x[1], reverse=True)

        for key, value in sorted_map:
            if k > 0:
                ans.append(key)
                k -= 1
        return ans
