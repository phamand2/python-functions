def is_odd(num):
  if not is_even(num):
    return True
  else:
    return False


def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False  


def odd_only(list_of_numbers):
    odds = []
    for number in list_of_numbers:
        if is_odd(number):
            odds.append(number)
    return odds

numbers_to_check = ([11, 20, 42, 97, 23, 10])

print(odd_only(numbers_to_check))