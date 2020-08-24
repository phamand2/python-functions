def shortest(list_of_strings):
  list_of_strings.sort(key=len)
  return(list_of_strings[0])

random_strings = ['Hello', 'Website', 'Jewlery', 'food']

print(shortest(random_strings))