



single_quote = 'hello'
double_quote = "WORLD"
triple_quote = """Multi-line
asd
asd
asd
string"""

print(single_quote)
print(double_quote)
print(triple_quote)

text = "Python Programming"

print(text[0])
print(text[ -1])
print(text[0:6])
print(text[ :6])
print(text[7: ])

name = " bob the builder "

print(len(name))
print(name.strip())
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("bob", "jane"))

name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old."             #f-string
message_2 = "My name is {} and I am {} years old.".format(name, age)    #str.format()
message_3 = "My name is %s and I am %d years old."% (name,age)         #%-formatting

print(message_1)
print(message_2)
print(message_3)



texts = """Python is a powerful programming language. It's easy to learn 
and versatile!
You can use Python for web development, data science and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""


print(len(texts))
