import math


def sort_array(arr):
    return sorted(arr)


def sorted_squared_num(arr):
    squared_arr = []
    for i in arr:
        squared_arr.append(int(math.pow(i, 2)))
    return sort_array(squared_arr)


a = [1, 3, 4, 5]
b = [-7, -2, 3, 4, 9]
c = []
print(sorted_squared_num(a))
print(sorted_squared_num(b))
print(sorted_squared_num(c))
