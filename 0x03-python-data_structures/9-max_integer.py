def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_val = my_list[0]  # Start by assuming the first number is the biggest

    for num in my_list:
        if num > max_val:
            max_val = num  # Found a bigger number, update max_val

    return max_val
