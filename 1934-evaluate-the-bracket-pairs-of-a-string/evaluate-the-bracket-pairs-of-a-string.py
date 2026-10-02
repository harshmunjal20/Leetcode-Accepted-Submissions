class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hashMap = {}

        for [key, value] in knowledge:
            hashMap[key] = value
        
        answer = [""]
        idx = 0
        sz = len(s)

        while idx < sz:
            if s[idx] == '(':
                temp = []
                idx += 1

                while idx < sz and s[idx] != ')':
                    temp.append(s[idx])
                    idx += 1
                
                key = "".join(temp)

                if key in hashMap:
                    answer.extend(hashMap[key])
                else:
                    answer.extend("?")
            else:
                temp = []

                while idx < sz and s[idx] != '(':
                    temp.append(s[idx])
                    idx += 1

                idx -= 1 # because idx is at '('
                answer.extend(temp)

            idx += 1


        return "".join(answer)