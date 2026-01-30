# for example
# lets print the numbers 1 to 10

for i in range(-10, 10, 2): # initial, end, step
    print(i)

# print multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()