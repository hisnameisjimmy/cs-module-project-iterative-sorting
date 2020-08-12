def linear_search(arr, target):
    # Your code here
    # Simple, loop through the array, for each loop see if the array is equal to the target, if yes, return true
    for i in range(len(arr)):
        # print(f'Index: {arr[i]}, Target: {target}')
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # Take the array length - 1, split it in half and get the value of that item
    # if it's equal, return it
    # if it's greater than the middle item, go right
    # if it's less than the middle item, go left
    # if you go left or right, you have to split that in half, and do the same thing again
    # In order to keep this going, we should probably use a while loop where a value is if it is successfully found

    not_found = True
    array_start_index = 0
    array_end_index = len(arr) - 1
    while not_found:
        middle_index = (array_start_index + array_end_index) // 2
        print(f'{middle_index}')
        if middle_index < 0:
            return -1  # not found
        elif arr[middle_index] == target:
            return middle_index
        elif target < arr[middle_index]:
            array_end_index = middle_index
        elif target > arr[middle_index]:
            array_start_index = middle_index
    
