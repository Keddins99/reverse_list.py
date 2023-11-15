def reverse_list(lst):
    length = len(lst)

    for i in range(length // 2):
        temp = lst[i]
        lst[i] = lst[length - 1 - i]
        lst[length - 1 - i] = temp

vals = [7, -3, 12, 9]
reverse_list(vals)
