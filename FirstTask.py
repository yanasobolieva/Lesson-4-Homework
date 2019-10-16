# First approach with using slice
my_first_string = "ecnalubma"[::-1]
print(my_first_string)


# Second approach with using function and slice
def reverse_function(word):
    return word[::-1]


functionResults = reverse_function("ecnalubma")

print(functionResults)
