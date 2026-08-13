class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp={}
        max_len=0
        leftIdx=0
        for index,ch in enumerate(s):

            if ch not in mapp:
                mapp[ch]=index
            else:
                if leftIdx<=mapp[ch]:
                    leftIdx=mapp[ch]+1
                mapp[ch]=index
            max_len=max(max_len,mapp[ch]-leftIdx+1)
        return max_len

