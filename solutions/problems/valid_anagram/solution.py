class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]] += 1
            else:
                dictionary[s[i]] = 1
        for i in range(len(t)):
            if t[i] in dictionary and dictionary[t[i]] != 0:
                dictionary[t[i]] -= 1
        sum = 0
        for value in dictionary.values():
            sum += value
        return sum == 0