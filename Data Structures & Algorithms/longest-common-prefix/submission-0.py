class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]

        for elem in strs:
            prefix = prefix[:len(elem)]
            for j in range(len(prefix)):
                if prefix[j] != elem[j]:
                    prefix = prefix[:j]
                    break
        
        return prefix