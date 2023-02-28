def calPoints(operations):
    
    score = []

    for top_of_stack in operations:

        if top_of_stack == '+':
            score.append(score[-1] + score[-2])

        elif top_of_stack == 'C':
            score.pop()
            
        elif top_of_stack == 'D':
            score.append(2 * score[-1])

        else:
            score.append(int(top_of_stack))

    return sum(score)
    
ops = ["5","2","C","D","+"]
print(calPoints(ops))
