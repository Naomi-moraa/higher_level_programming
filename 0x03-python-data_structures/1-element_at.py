def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
my_list=[1,2,3,4,5]
print (element_at(my_list, 2))
