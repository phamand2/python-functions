def longest(list_of_strings):
  list_of_strings.sort(key=len)
  return list_of_strings[-1]

random_strings = ['Hello', 'Website', 'Jewlery', 'food']

print(longest(random_strings)) 