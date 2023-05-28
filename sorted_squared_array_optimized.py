import math


def sort_array(arr):
    return sorted(arr)


def sorted_squared_arr(arr):
    # initialize an empty array with same size as input array
    new_arr = [0] * len(arr)
    # now we know the max value when we square a number will either be 0th index or last index , as at 0th index the
    # max -ve value will be there and since square of -ve is positive ,and same goes to last element since it will be
    # biggest since it is the sorted array
    pointer_left = 0
    pointer_right = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        left_square = arr[pointer_left] * arr[pointer_left]
        rt_square = arr[pointer_right] * arr[pointer_right]
        if left_square > rt_square:
            new_arr[i] = left_square
            pointer_left += 1
        else:
            new_arr[i] = rt_square
            pointer_right -= 1
    return new_arr


a = [1, 3, 4, 5]
b = [-7, -2, 3, 4, 9]
c = []
print(sorted_squared_arr(a))
print(sorted_squared_arr(b))
print(sorted_squared_arr(c))
