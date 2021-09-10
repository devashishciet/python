num = int(input("Enter the limit- "))
num_sum = 0
for i in range(num+1):
    if i % 2 != 0:
        num_sum += (i**2)
print(f"The sum of square of the odd number is- {num_sum}")
