from argparse import ArgumentParser
from datetime import datetime
import math
import random
import sorting

INSERTION_SORT = 'insertion_sort'
algorithm_choices = [INSERTION_SORT]

parser = ArgumentParser('Test different sorting algorithms. You can pass a list of elements or a number of elements')

parser.add_argument('-a', dest='algorithm', required=True, choices=algorithm_choices)
parser.add_argument('-l', dest='array', nargs='*')
parser.add_argument('-n', dest='number_of_elements', type=int)

args = parser.parse_args()

algorithm = args.algorithm
array = args.array
number_of_elements = args.number_of_elements

if array is None and number_of_elements is None:
    print('You must define a list or a number of elements')
    exit()

if array is None:
    array = []

    for i in range(number_of_elements):
        array.append(math.floor(100 * random.random()))

show_array = len(array) <= 100

if show_array:
    print('Input array:')
    print(array)

start_time = datetime.now()

sorted_array = []
if algorithm == INSERTION_SORT:
    sorted_array = sorting.insertion_sort(array)

end_time = datetime.now()

if show_array:
    print('Output array:')
    print(sorted_array)

print('\nSorting time: ' + str(end_time - start_time))