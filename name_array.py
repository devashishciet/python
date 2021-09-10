name = input("Enter the names separated by comma- ")
name_array = []
name_array = name.split(",")
for i in range(len(name_array)):
    print(name_array[i].capitalize())
