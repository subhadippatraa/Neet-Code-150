class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        mapp={}

        for ch in s:
            mapp[ch]=mapp.get(ch,0)+1
        
        for ch in t:
            if ch not in mapp:
                return False
            mapp[ch]-=1
            if(mapp[ch]<0):
                return False
        return True

        
