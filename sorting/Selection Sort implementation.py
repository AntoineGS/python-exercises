# Basic implementation of selection sor for an array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


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


print(selection_sort(numbers))