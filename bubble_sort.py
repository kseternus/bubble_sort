def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return print(f'Sorted array: {arr}')


num_list = [40, 9, 21, 48, 36, 97, 67, 35, 17, 38, 29, 4, 23, 0, 80, 16, 16, 30, 96, 13, 74, 58, 86, 2, 18]
bubble_sort(num_list)
