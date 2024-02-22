def fizz_buzz(param):
  #Type your code here
  if param % 3 == 0 and param % 5 == 0:
    result = "FizzBuzz"
  elif param % 3 == 0:
    result = "Fizz"
  elif param % 5 == 0:
    result = "Buzz"
  else:
    result = str(param)
    return result


