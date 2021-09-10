def square(m, n):
    return m*n


# def cube(n):
#     return n**3


lists = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
final_list = map(square, lists, list2)
print(list(final_list))
