s = input("Enter a string: ")

# Convert string to listA
s_list = list(s)
print("Your String: ",s)

# Reverse the list
s_list.reverse()

# Convert list back to string
reversed_string = ''.join(s_list)  # Join the list back into a string

print("Reversed string:", reversed_string)

if s==reversed_string:
    print("Palinedrome")
else:
    print("Not palindorme")