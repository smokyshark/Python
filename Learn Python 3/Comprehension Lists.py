# Your code below:
single_digits = range(0,10)
squares = []
for i in single_digits:
  print(i)
  squares.append(i ** 2)
print(squares)
cubes = [i ** 3 for i in single_digits]
print(cubes)