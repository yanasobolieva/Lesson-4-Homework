def reverse_words(initial_input):
    input_str = initial_input.split(" ")
    input_str = input_str[-1::-1]
    output_result = ' '.join(input_str)
    return output_result


input_string = "one two three four"
print(input_string)
print(reverse_words(input_string))
