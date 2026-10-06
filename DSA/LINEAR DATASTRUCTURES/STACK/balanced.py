'''wap using stack to check the given paranthesis is balanced or not'''


def balanced_paranthesis(s1):
    stack=[]
    values = { 
    ']':'[',
    ')':'(',
    '}':'{'
    }

    for char in s1:
            if char in "[({":
                stack.append(char)
            elif char in "])}":
                if not stack or stack.pop()  != values[char]:
                    return False
    return len(stack) == 0

s = "[][]{{}}"
if balanced_paranthesis(s):
    print("Balanced")
else:
    print("Not Balanced")












