# bounce.py
#
# Exercise 1.5

def bounce(height, n):
  starting_height = height
  for i in range(n):
    starting_height = starting_height * 0.6
    print(i, round(starting_height, 4))
    
bounce(100, 10)