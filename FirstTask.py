# First approach with using slice
def reverse_with_slice_function(some_word):
    return some_word[::-1]


my_first_result = reverse_with_slice_function("ecnalubma")
print(my_first_result)


# Second approach with using loop
def reverse_with_loop_function(some_string):
    reversed_list_from_string = []
    index = len(some_string)
    while index > 0:
        reversed_list_from_string += some_string[index - 1]
        index -= 1
    reversed_string = str("".join(reversed_list_from_string))
    return reversed_string


my_second_result = reverse_with_loop_function("ecnalubma")
print(my_second_result)