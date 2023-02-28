target_list = [1, 3, 5, 3, 5, 7, 8, 0, 9, 2, 4]

def linear_search(list, number):
    counter = 0
    while counter <= len(list):
        if list[counter] == number:
            return counter
        else:
            counter +=1

def linear_search_2(list, number):
    for search in range(len(list)):
        if number == list[search]:
            return search
        else:
            search += 1
            

print(linear_search(target_list, 5))
print(linear_search_2(target_list, 1))
