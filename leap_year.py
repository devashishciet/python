year = input("Enter the year- ")
if year[-1] == 0 and year[-2]:
    if int(year) % 400 == 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
elif int(year) % 4 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
