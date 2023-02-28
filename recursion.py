def calculate_factorial(number):
    for n in range(number, 2, -1):
        number *= (n-1)
    return number

print(calculate_factorial(6))

    

def recursive_factorial(number):
    if (number==0 or number==1):
        return 1
    else:
        return (number * recursive_factorial(number -1))

number = 5
print(recursive_factorial(number))
