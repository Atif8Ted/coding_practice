def is_monotonic(arr):
    if len(arr) <= 1:
        return True
    # case when 0th and last element of an array is same
    if arr[0] == arr[-1]:
        res = all(ele == arr[0] for ele in arr)
        return res
    # case:2 when last element of the array is larger than 0th element.
    # in  this case we have to prove that the array is monotonically increasing , if not return false.
    if arr[0] < arr[-1]:
        # print("in this")
        for i in range(len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                # print("in this if")
                pass
            else:
                # print("in this else")
                return False
        # return True
    # case3: monotonically decreasing:
    if arr[0] > arr[-1]:
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                pass
            else:
                return False
    return True


print(is_monotonic([1, 2, 3, 4, 5, 5]))
#
print(is_monotonic([1, 1, 1, 1, 1, 1]))
print(is_monotonic([1, -2, -3, -4, -5, -6]))

print(is_monotonic([1, -2, 3, -4, -5, -6]))

print(is_monotonic([]))
print(is_monotonic([1, -2, 3, -4, -5, -6, -1]))
