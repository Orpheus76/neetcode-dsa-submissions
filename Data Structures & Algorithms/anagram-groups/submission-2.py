class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = collections.defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            wordMap[sorted_word].append(word)
        
        return list(wordMap.values())