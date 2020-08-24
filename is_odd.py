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


while True:
  num = int(input('Give me a numer to check if it is odd: '))
  check_odd= is_odd(num)
  print(check_odd)    