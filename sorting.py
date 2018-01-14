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
