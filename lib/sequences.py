#!/usr/bin/env python3
def print_fibonacci(length):
  if length == 0:
    print([])
  elif length == 1:
    print([0])
  else:
    fibo = [0,1]
    for _ in range(length-2):
      fib = fibo[-1] + fibo[-2]
      fibo.append(fib)
    print(fibo)