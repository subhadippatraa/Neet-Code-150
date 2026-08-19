class Solution:

    def helper(self, index, candidates, target, temp, ans):

        if target == 0:
            ans.append(temp.copy())
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            temp.append(candidates[i])
            self.helper(
                i + 1,
                candidates,
                target - candidates[i],
                temp,
                ans
            )
            temp.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        temp = []
        ans = []

        self.helper(0, candidates, target, temp, ans)

        return ans