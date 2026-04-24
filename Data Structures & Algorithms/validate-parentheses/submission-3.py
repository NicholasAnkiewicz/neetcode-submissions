class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in "(":
                stack.insert(0,")")
            elif c in "[":
                stack.insert(0,"]")
            elif c in "{":
                stack.insert(0,"}")
            elif c in "}])":
                if len(stack) == 0:
                    return False
                if c != stack.pop(0):
                    return False
        if len(stack) != 0:
            return False
        return True
