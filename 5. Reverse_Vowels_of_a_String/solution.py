class Solution:
    def reverseVowels(self, s: str) -> str:
        split_characters = list(s)
        vowels = []
        result = []

        for char in split_characters:
            if char in "aeiouAEIOU":
                vowels.append(char)

        vowels.reverse()

        vowel_index = 0

        for char in split_characters:
            if char in "aeiouAEIOU":
                result.append(vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)

        return "".join(result)
