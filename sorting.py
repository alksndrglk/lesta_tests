def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


"""
Не смотря на S(n) по памяти, аглоритм слияния показывает О(nlogn) даже в самом худшем случае.
Учитывая, что алгоритм является стабильным, он не будет делать лишних сравнений и перестановок, если на вход поступит отсортированный массив.
"""
