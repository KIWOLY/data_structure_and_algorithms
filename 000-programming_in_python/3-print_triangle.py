def print_right_triangle(height):
    if height == 0:
        return None
    for i in range(1, height + 1):
        print('*' * i)


if __name__=="__main__":
     height=int(input("enter a number: "))
     print_right_triangle(height)
