class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for i, word in enumerate(strs):
            parsed_word = "".join(sorted(word))
            
            if parsed_word not in anagrams:
                indexes = []
            else:
                indexes = anagrams[parsed_word]
            indexes.append(i)
            anagrams[parsed_word] = indexes

        res = []
        for _, indexes in anagrams.items():
            res.append([strs[i] for i in indexes])

        return res