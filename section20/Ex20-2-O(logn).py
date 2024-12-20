"""
파일명: Ex20-2-O(logn)

O(logN)
    로그 시간 복잡도, 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘

"""

def binary_search(arr, x):

    low = 0

    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# 실행코드
arr = [1, 10, 5, 7, 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 11))






















