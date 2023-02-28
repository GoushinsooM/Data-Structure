def selection_sort(list, size):
    for index in range(size):
        minor_number = index

        for number in range(index + 1, size):
            if to_order[number] < to_order[minor_number]:
                minor_number = number

        (to_order[index], to_order[minor_number]) = (to_order[minor_number], to_order[index])


to_order = [1, 3, 5, 3, 5, 7, 8, 0, 9, 2, 4]
size = len(to_order)
# print(to_order)
# selection_sort(to_order, size)
