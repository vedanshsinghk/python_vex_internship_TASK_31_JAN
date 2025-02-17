#q1
# Create a Python program to convert temperatures between Celsius and Fahrenheit.
def Cel_to_Fahr(celsius):
    return celsius*9/5+32
def far_to_cel(fahr):
    return (fahr - 32) * 5/9
def main():
    temp=int(input("Enter your number in Degres: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    if unit == 'C':
        converted_temp= Cel_to_Fahr(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit=='F':
        converted_temp=far_to_cel(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Please enter Valid input, Either 'C' or 'F' specially in Upper case")
        
if __name__ == "__main__":
    main()
