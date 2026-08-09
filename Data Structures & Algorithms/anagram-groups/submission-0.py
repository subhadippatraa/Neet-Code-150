class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapp={}
        for strr in strs:
            key=''.join(sorted(strr))
            if key not in mapp:
                mapp[key]=[]
            mapp[key].append(strr)
        return list(mapp.values())

        
        

