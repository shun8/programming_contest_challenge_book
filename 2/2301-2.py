n = 4
wv = [(2, 3), (1, 2), (3, 4), (2, 2)]
w = 5

dp = [[0 for j in range(w+1)] for i in range(n)]

def solve():
  for i in range(0, n):
    for wi in range(0, w+1):
      if wi == 0:
        dp[i][wi] = 0
        continue
      if i == 0 and wi < wv[i][0]:
        dp[i][wi] = 0
        continue
      if i == 0 and wi >= wv[i][0]:
        dp[i][wi] = wv[i][1]
        continue

      if wi < wv[i][0]:
        dp[i][wi] = dp[i-1][wi]
        continue
      dp[i][wi] = max(dp[i-1][wi], dp[i-1][wi-wv[i][0]]+wv[i][1])

  return dp[n-1][5]

print("{}".format(solve()))
