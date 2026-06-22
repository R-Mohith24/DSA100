def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    ans = len(arr)   # default if not found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1   # go left
        else:
            low = mid + 1    # go right

    return ans


def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    ans = len(arr)   # default if not found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > target:
            ans = mid
            high = mid - 1   # go left
        else:
            low = mid + 1    # go right

    return ans