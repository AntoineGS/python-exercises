numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# Basic implementation of selection sort for an array, pretty inefficient
def selection_sort(array):
    for i in range(len(array)):
        # Until proven otherwise i is the min (used to both initialize the values and skip the first iteration
        min_value_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_value_index]:
                min_value_index = j

        if i != min_value_index:
            temp_value = array[i]
            array[i] = array[min_value_index]
            array[min_value_index] = temp_value

    return array


# Bubble sort, also pretty inefficient
def bubble_sort(array):
    for max_index in reversed(range(len(numbers))):
        for curr_index in range(max_index):
            if array[curr_index] > array[curr_index + 1]:
                temp_value = array[curr_index]
                array[curr_index] = array[curr_index + 1]
                array[curr_index + 1] = temp_value

    return array


# Algorithm for when you know list is sorted or almost sorted (can get O(n))
def insertion_sort(array):
    if len(array) < 2:
        return array  # exit here, nothing to sort

    # Since arrays are lists in Python, we can splice them and put them back together instead of moving all values
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:  # if False then it is already ordered, so we leave it there
            for j in range(0, i):  # loop through the already processed values
                if array[i] < array[j]:
                    array = array[:j] + [array[i]] + array[j:i] + array[i + 1:]
    return array


# Merge sort!
def merge_sort(array):
    length = len(array)

    # Exits when at lower size, exiting the recursion loop
    if length == 1:
        return array

    # Split Array in into right and left
    left = array[:int(length/2)]  # rounds down
    right = array[int(length/2):]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    array = []
    left_length = len(left)
    right_length = len(right)
    left_index = 0
    right_index = 0

    while True:
        if (left_index < left_length) and ((right_index == right_length) or (left[left_index] < right[right_index])):
            array.append(left[left_index])
            left_index += 1
        elif (right_index < right_length) and ((left_index == left_length) or (right[right_index] < left[left_index])):
            array.append(right[right_index])
            right_index += 1
        else:
            return array


# print(selection_sort(numbers))
# print(bubble_sort(numbers))
# print(insertion_sort(numbers))
print(merge_sort(numbers))
