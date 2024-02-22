def fizz_buzz(param):
  #Type your code here
  if param % 3 :
    return 'Fizz'
  elif param % 5 :
    return 'Buzz'
  elif param % 3 and param % 5 :
    return 'FizzBuzz'
  else:
    result = str(param)
    return result


