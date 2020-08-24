def c_to_f (celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

celsius = int(input('Give me a degree in celsius: '))  

f_conversion = c_to_f(celsius)
print(f'The converision from {celsius} degree celsius to Fahrenheit is {f_conversion}.')