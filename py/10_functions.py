
#Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Abubakar")

#Function with return parameters

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)   

#Default parameters

def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"


print(greet_with_title("Smith" ))
print(greet_with_title("Johnson", "Dr."))

#*args -variable number of arguments

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

#**kwargs - keyword arguments

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

#combining *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

#Lambda function(anonymous function)

square = lambda x: x ** 2
print(square(5))

add = lambda x, y: x + y
print(add(3, 4))    

