class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for ch in s:
            if len(stack)==0 :
                if ch not in "({[":
                    return False
                else:
                    stack.append(ch)
            else:
                if(stack[-1] in "({[" and ch in ")}]"):
                    if (
                        (stack[-1] == '(' and ch == ')')
                        or (stack[-1] == '{' and ch == '}')
                        or (stack[-1] == '[' and ch == ']')
                    ):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(ch)
        return len(stack)==0

            