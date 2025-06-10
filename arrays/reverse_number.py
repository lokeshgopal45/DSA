def is_reverse_array(arr):
    """Checking reverse array."""
    is_reverse = True
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i]:
            pass
        else:
            is_reverse = False
            break
    return is_reverse

arr = [2,3,1,4,5]
print(is_reverse_array(arr))