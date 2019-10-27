def replace_digits_in_list(digit_list):
    for i in range(len(digit_list)):
        if digit_list[i] < 0:
            digit_list[i] = -1
        elif digit_list[i] > 0:
            digit_list[i] = 1
    return digit_list


initial_list = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
print(initial_list)
print(replace_digits_in_list(initial_list))
