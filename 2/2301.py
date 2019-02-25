n = 4
wv = [(2, 3), (1, 2), (3, 4), (2, 2)]
w = 5

def calc(i, wi):
  if i >= n:
    return 0

  v1 = calc(i+1, wi)
  if wi-wv[i][0] >= 0:
    v2 = calc(i+1, wi-wv[i][0]) + wv[i][1]

  if wi-wv[i][0] >= 0 and v2 > v1:
    return v2
  return v1

def solve():
  ans = calc(0, w)
  return ans

print("{}".format(solve()))
