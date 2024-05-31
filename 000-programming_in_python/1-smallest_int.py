def get_smallest_integer(my_list):
    if not my_list:
       return None
    smallest = my_list[0]
    for num in my_list:
        if num < smallest:
            smallest = num
    return smallest

# Example usage:
if __name__== "__main__":
   my_list = [20,5,4,8,9]
   print(get_smallest_integer(my_list))

    



    

    
