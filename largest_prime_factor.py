from math import sqrt

def isPrime(n):
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

VALUE = 600851475143
factors = []
prime_factors = []

for i in range(2, int(sqrt(VALUE))):
  if VALUE % i == 0:
    factors.append(i)
    factors.append(VALUE // i)

for factor in factors:
  if isPrime(factor):
    prime_factors.append(factor)
    
print(max(prime_factors))