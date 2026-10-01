class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i, j = 0, 0

        while j < len(s):
            if s[j] != " ":
                j += 1
            else:
                if i != j:
                    word = s[i : j]
                    ans.append(word)

                while j < len(s) and s[j] == " ":
                    j += 1
                
                i = j
            
        if i != j:
            word = s[i : j]
            ans.append(word)
        
        ans = ans[::-1]
        return " ".join(ans)