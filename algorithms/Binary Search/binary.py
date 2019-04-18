lst = range(0, 100)
searched_value = 56


def binary_search(arr, start, length, search_value):
    if length > 1:
        mid = int(start + (length - start) / 2)
        if search_value == arr[mid]:
            return mid
        if arr[mid] > search_value:
            return binary_search(arr, start, mid - 1, search_value)
        elif arr[mid] < search_value:
            return binary_search(arr, mid + 1, length, search_value)
    else:
        return -1


print(binary_search(lst, 0, len(lst), searched_value))