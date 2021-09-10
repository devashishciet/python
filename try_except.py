try:
    a = int(input("Enter a "))
    b = int(input("Enter b "))
    c = a/b
    print(c)
except Exception as e:
    print(f"error:  {e}")
else:
    print("Completed!")

finally:
    print("Programme stopped!")
