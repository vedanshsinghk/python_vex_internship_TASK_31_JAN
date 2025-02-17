# Input a tuple of numbers
t = tuple(map(int, input("Enter a tuple of numbers separated by spaces: ").split()))

# Swap two numbers in the tuple (example: swap the first and second elements)
swap = (t[-1],) + t[1:-1] + (t[0],)
print("Original tuple:", t)
print("Tuple after swapping:", swap)