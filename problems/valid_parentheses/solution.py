class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # If empty add
            # If get a match pop out of the stack
            # Else also add
            if not stack:
                stack.append(char)
            elif stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            elif stack[-1] == "{" and char == "}":
                stack.pop()
            else:
                stack.append(char)
        # If stack empty - Mission successful
        if not stack:
            return True
        return False
                
