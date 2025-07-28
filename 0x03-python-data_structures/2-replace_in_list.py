def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

# Example usage
my_list = [1, 2, 3, 4, 5]
updated_list = replace_in_list(my_list, 3, 9)
print(updated_list)
