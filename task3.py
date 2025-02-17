# Input a list of numbers
numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
number_list=list(map(int,numbers.split()))

print("List of numbers:", number_list)

s=max(number_list)
print("Your largest number is: ",s)