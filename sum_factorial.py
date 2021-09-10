num = int(input("Enter the limit- "))
num_sum = 0
fact_num = 1
for i in range(1, num+1):
    fact_num *= i
    num_sum += fact_num
print(f"The sum is {num_sum}")
