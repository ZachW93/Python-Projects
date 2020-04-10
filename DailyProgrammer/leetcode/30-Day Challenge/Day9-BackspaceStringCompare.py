class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def backspace(word):
            length = len(word)
            result = ''
            i = 0
            
            for j in range(length - 1, -1, -1):
                if word[j] == '#':
                    i += 1
                elif i > 0:
                    i -= 1
                else:
                    result = word[j] + result
            
            return result
    
        return backspace(S) == backspace(T)
    