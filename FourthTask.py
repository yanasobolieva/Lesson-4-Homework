# Create function to fill some list with digits
def fill_list_with_digits(start, end, step):
    some_list = []
    for i in range(start, end, step):
        some_list.append(i)
    return some_list


# Create function to count even and odd digits in list
def count_even_and_odd(digits_list):
    even_count = 0
    odd_count = 0
    for dig in digits_list:
        if dig % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


my_list = fill_list_with_digits(1, 999999, 8)
print(my_list)

(even_count, odd_count) = count_even_and_odd(my_list)
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
