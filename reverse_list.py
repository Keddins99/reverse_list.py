def reverse_list(data_list):
    i, j = 0, len(data_list) - 1
    while i < j:
        data_list[i], data_list[j] = data_list[j], data_list[i]
        i += 1
        j -= 1


vals = [7, -3, 12, 9]
reverse_list(vals)
print(vals)
