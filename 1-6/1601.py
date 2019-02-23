n = 5
a = [2, 10, 11, 100, 10000]
a.sort(reverse=True)

def solve():
  for i in range(0, n-2):
    if a[i] < a[i+1] + a[i+2]:
      return a[i] + a[i+1] + a[i+2]

  return 0

print("{}".format(solve()))
