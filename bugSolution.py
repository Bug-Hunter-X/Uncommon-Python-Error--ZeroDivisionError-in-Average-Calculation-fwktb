def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if 0 in numbers and len(numbers) == sum(1 for x in numbers if x == 0):
        return 0 #Handle list with only zeros
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of empty list is: {average_empty}")

my_list_with_zero = [1, 0, 2, 3, 4]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zero is: {average_with_zero}")

my_list_only_zeros = [0, 0, 0]
average_only_zeros = calculate_average(my_list_only_zeros)
print(f"The average of only zeros is: {average_only_zeros}") 