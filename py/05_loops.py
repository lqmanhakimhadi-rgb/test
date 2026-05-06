
# #For Loops
# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)    

# #While Loops
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(10):
#     if i ==3:
#         continue    
#     if i == 7:
#         break
#     print(i)


# for i in range(2):
#     for j in range(3):
#         print(f"({i}, {j})")


number = 5
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

limit = 20

for num in range(2, limit + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)