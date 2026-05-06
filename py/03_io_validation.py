#Input and Output Validation

name =str(input("Enter your name: "))
height = float(input("Enter your height: "))

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0 and age <500:
            break
        else:
            print("Please enter a valid number!")
    except ValueError:
        print("Please enter a valid number!")



print(f"Hello, {name}")
print(f"You are {age} years old and {height} feet tall.")

