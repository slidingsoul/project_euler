def fibonacci(n):
  if n == 1 or n == 2:
    return n
  return fibonacci(n - 2) + fibonacci (n - 1)

# print(fibonacci(3))
END = 4_000_000
a = 0
b = 1
n = 0
result = 0
while n < END:
  n = a + b
  a = b
  b = n
  if n % 2 == 0:
    result += n
print(result)