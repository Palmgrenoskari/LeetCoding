class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Take shortest string
        prefix = min(strs, key=len)
        # Loop strings and check if we can find a string that doesn't share the whole prefix
        # Then drop one letter from the prefix and start again.
        # Continue until all strings share the same prefix or the word has reduced to nothing
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

        # @juisunitadileeppatil

