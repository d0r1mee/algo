def get_x_from_merged_arrays(x):
    arr1_index, arr2_index = 1, 1
    current_position = 0

    while True:
        current_position += 1
        
        if arr1_index ** 2 > arr2_index ** 3:
            if current_position == x:
                return arr2_index ** 3
            arr2_index += 1
        elif arr1_index ** 2 < arr2_index ** 3:
            if current_position == x:
                return arr1_index ** 2
            arr1_index += 1

        else: 
            if current_position == x:
                return arr1_index ** 2
            arr1_index += 1
            arr2_index += 1

    # return merged_arrays[x - 1]

x = int(input())

print(get_x_from_merged_arrays(x))


        