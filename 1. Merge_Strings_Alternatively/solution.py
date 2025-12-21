class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ''
        i = 0
        j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged_word += word1[i]
                i+=1
            if j < len(word2):
                merged_word += word2[j]
                j+=1

        return merged_word