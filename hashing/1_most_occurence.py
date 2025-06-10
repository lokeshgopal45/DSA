def most_occurence_elements(input_arr):
    """Basic question in Hashing without any precompuatation"""
    ans_arr = {}
    for i in input_arr:
        if i in ans_arr:
            ans_arr[i] += 1
        else:
            ans_arr[i] = 1
    return ans_arr

arr = [1,2,3,4,4,4,4]
print(most_occurence_elements(arr))