# Create empty list
test_list = []

# Fill in the list
for i in range(1, 999999, 8):
    test_list.append(i)

print(test_list)

# Count even and odds
even_count = 0
odd_count = 0

for dig in test_list:
    if dig % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print results
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
