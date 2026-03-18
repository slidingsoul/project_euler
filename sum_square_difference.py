END = 100

square_sum = ((100 // 2) * ((2 * 1) + ((100 - 1) * 1))) ** 2

sum_square = 0

for i in range(1, END + 1):
  sum_square += i ** 2
  
print(abs(square_sum - sum_square))