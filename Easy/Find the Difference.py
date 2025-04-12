class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        countS = Counter(s)
        countT = Counter(t)

        for letter in countT:
            if letter not in countS:
                return letter
            elif countS[letter] != countT[letter]:
                return letter
            
        # - Count letters in both strings
        # - Loop through letters in t
        # - If a letter is new or occurs more times in t, it's the extra one