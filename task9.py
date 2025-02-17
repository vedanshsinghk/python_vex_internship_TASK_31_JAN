def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Return 0 to handle empty list case
    return sum(numbers) / len(numbers)

numbers = [2, 4, 6, 8, 10]
average = calculate_average(numbers)
print(average)
