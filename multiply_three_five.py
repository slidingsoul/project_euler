res = 0
END = 1000
for i in range(1, END):
  if i % 3 == 0 or i % 5 == 0:
    res += i
print(res)