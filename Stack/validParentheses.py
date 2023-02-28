def isValid(string):
    stack = []
    to_close = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for top in string:        
        print(top)
    return True


string = '()'
print(isValid(string))