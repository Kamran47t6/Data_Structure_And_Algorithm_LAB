 
def CountSort(input_arr):
    min_val = min(input_arr)
    max_val = max(input_arr)
    
    # Create a counting array to store the frequency of each value in the given range.
    count_arr = [0] * (max_val - min_val + 1)
    
    # Count the occurrences of each value in the input array.
    for num in input_arr:
        count_arr[num - min_val] += 1

    # Reconstruct the sorted output array.
    output_array = []
    for i, count in enumerate(count_arr):
        output_array.extend([i + min_val] * count)
    
    return output_array

input_arr = [0, 9, 2, -10, 1, 8, 7]
result = CountSort(input_arr)
print(result)


