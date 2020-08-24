def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

while True:
  num = int(input('Give me a numer to check if it is even: '))
  check_even = is_even(num)
  print(check_even)