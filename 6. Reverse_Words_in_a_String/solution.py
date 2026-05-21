class Solution:
    def reverseWords(self, s: str) -> str:
        split_words = s.split()
        split_words.reverse()
        return " ".join(split_words)