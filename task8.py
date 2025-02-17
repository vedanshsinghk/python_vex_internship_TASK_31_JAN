# Function calculate the sum of even numbers
def sum_of_even_numbers(n):
    total_sum = 0
    
    for i in range(2, n+1, 2):  # Start from 2, go up to n, step by 2 (even numbers)
        total_sum += i
        
    return total_sum

n = int(input("Enter a number n: "))

result = sum_of_even_numbers(n)
print(f"The sum of all even numbers from 1 to {n} is {result}.")
