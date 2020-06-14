def bubble_sort(arr_list):
    has_swapped = True

    while has_swapped:
        has_swapped = False
        i = 0  # no of iteration
        n = len(arr_list)
        for i in range(0, n - i - 1):
            if arr_list[i] > arr_list[i+1]:
                # Swap
                arr_list[i], arr_list[i+1] = arr_list[i+1], arr_list[i]
                has_swapped = True
        i += 1
    return arr_list


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split(" ")))
    print(bubble_sort(arr))

