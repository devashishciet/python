def prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
        else:
            return True

#Filter method
num = int(input("Enter the limit- "))
filtered = filter(prime, range(num))
print(f"The prime number llist are- {list(filtered)}")
