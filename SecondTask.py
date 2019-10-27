def reverse_words(initial_input):
    return ' '.join(initial_input.split(" ")[-1::-1])


input_string = "one two three four"
print(input_string)
print(reverse_words(input_string))
