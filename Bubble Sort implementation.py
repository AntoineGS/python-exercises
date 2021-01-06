# Basic implementation of a bubble sort

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubble_sort(array):
    for max_index in reversed(range(len(numbers))):
        for curr_index in range(max_index):
            if array[curr_index] > array[curr_index + 1]:
                temp_value = array[curr_index]
                array[curr_index] = array[curr_index + 1]
                array[curr_index + 1] = temp_value

    return array


print(bubble_sort(numbers))
