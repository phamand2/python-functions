def even_only(list_of_numbers):
    evens = []
    for number in list_of_numbers:
        if is_even(number):
            evens.append(number)
    return evens

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False


numbers_to_check = ([11, 20, 42, 97, 23, 10])

print(even_only(numbers_to_check))

