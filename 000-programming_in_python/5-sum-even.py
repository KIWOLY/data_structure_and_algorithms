def sum_even_numbers(my_list):
    even_sum = 0

    for num in my_list:
        if num % 2 == 0:
            even_sum += num
    return even_sum

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5, 6]
  print(sum_even_numbers(my_list))
