from cProfile import run
from timeit import timeit

def first_dup(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                print(arr[i], "is a duplicate")
                break

def my_func(arr):
    pass

my_arr = [4, 5, 7, 8, 3, 2, 21, 23, 34, 44, 22, 56, 76, 89, 90, 43, 5]

run_first_dup = timeit(lambda: first_dup(my_arr), number=20)

print(f'Time to run this function is {run_first_dup:.8f}')

