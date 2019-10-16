digits_list = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
print(digits_list)

for i in range(len(digits_list)):
    if digits_list[i] < 0:
        digits_list[i] = -1
    elif digits_list[i] > 0:
        digits_list[i] = 1

print(digits_list)
