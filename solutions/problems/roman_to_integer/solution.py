class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        # Symbols to numbers
        roman = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Loop length-1 times
        for i in range(len(s) - 1):
            # If next letter is bigger then substract the first letter: IV = -1+5
            if roman[s[i]] < roman[s[i+1]]:
                sum -= roman[s[i]]
            # Else then just add this letter
            else:
                sum += roman[s[i]]
        # Add last symbol
        return sum + roman[s[-1]]
        
