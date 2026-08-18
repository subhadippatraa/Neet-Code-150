class Solution:
    def helper(self, ans, open, close, temp, size):

        if len(temp) == size * 2:
            ans.append("".join(temp))
            return

        if open < size:
            temp.append('(')
            self.helper(ans, open + 1, close, temp, size)
            temp.pop()

        if close < open:
            temp.append(')')
            self.helper(ans, open, close + 1, temp, size)
            temp.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        self.helper(ans, 0, 0, [], n)

        return ans