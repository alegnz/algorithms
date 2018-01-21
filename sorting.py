import math
import sys


def insertion_sort(array):
    # elements in array[0..i-1] will be always sorted
    for i in range(1, len(array)):
        key = array[i]

        # Compares key with the elements in array[0..i-1]
        # until it founds an element smaller than key
        j = i - 1
        while j >= 0 and array[j] > key:
            # Moves every element greater than key in array[0..i-1] one step to the right
            array[i] = array[j]
            j -= 1
        array[j+1] = key

    return array


def merge_sort(array):
    begin = 0
    end = len(array)

    merge_sort_parameters(array, begin, end)

    return array


def merge_sort_parameters(array, begin, end):

    if begin < end:
        cut = math.floor((begin + end) / 2)

        if cut != begin:
            merge_sort_parameters(array, begin, cut)
            merge_sort_parameters(array, cut, end)

            merge(array, begin, cut, end)


def merge(array, begin, cut, end):
    left = array[begin:cut]
    right = array[cut:end]

    # Adds infinite numbers to the end of each list
    # to avoid checking when it gets to the end of the list
    left.append(sys.maxsize)
    right.append(sys.maxsize)

    i = 0
    j = 0

    for k in range(begin, end):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j +=1
