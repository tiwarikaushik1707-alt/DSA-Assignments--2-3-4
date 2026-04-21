import time
import random
import sys

sys.setrecursionlimit(20000)

# Sorting Algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Timing Function
def measure_time(sort_func, arr, is_quick=False):
    temp = arr.copy()

    start = time.time()

    if is_quick:
        sort_func(temp, 0, len(temp) - 1)
    else:
        result = sort_func(temp)
        if result is not None:
            temp = result

    end = time.time()

    return (end - start) * 1000


# Dataset Generator
def generate_random(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted(size):
    return list(range(size))


def generate_reverse(size):
    return list(range(size, 0, -1))


# Correctness Check
def correctness_check():
    test = [5, 2, 9, 1, 5, 6]

    arr1 = test.copy()
    insertion_sort(arr1)

    arr2 = merge_sort(test.copy())

    arr3 = test.copy()
    quick_sort(arr3, 0, len(arr3) - 1)

    return arr1, arr2, arr3


# Main Function
def main():
    random.seed(42)

    sizes = [1000, 5000, 10000]
    datasets = {
        "Random": generate_random,
        "Sorted": generate_sorted,
        "Reverse": generate_reverse
    }

    with open("output.txt", "w") as f:

        # Correctness Check
        ins, mer, qui = correctness_check()
        f.write("Correctness Check:\n")
        f.write(f"Insertion: {ins}\n")
        f.write(f"Merge: {mer}\n")
        f.write(f"Quick: {qui}\n")
        f.write("-" * 50 + "\n\n")

        print("Correctness Check:")
        print("Insertion:", ins)
        print("Merge:", mer)
        print("Quick:", qui)
        print("-" * 50)

        # Experiments
        for dtype, func in datasets.items():
            for size in sizes:
                data = func(size)

                t1 = measure_time(insertion_sort, data)
                t2 = measure_time(merge_sort, data)
                t3 = measure_time(quick_sort, data, is_quick=True)

                output = (
                    f"Input: {dtype} | Size: {size}\n"
                    f"Insertion Sort: {t1:.2f} ms\n"
                    f"Merge Sort: {t2:.2f} ms\n"
                    f"Quick Sort: {t3:.2f} ms\n"
                    + "-" * 50 + "\n"
                )

                print(output)
                f.write(output)


# Run Program
if __name__ == "__main__":
    main()