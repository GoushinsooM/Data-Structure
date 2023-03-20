def isValid(string):
    stack = []
    to_close = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for top in string:
        if top in to_close:
            if stack and stack[-1] == to_close[top]:
                stack.pop()
            else:
                return False
        else:
            stack.append(top)
    return True if not stack else False


string = "()[]{}"
print(isValid(string))