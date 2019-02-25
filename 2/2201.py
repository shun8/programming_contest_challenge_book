import heapq

n = 3
l = [8, 5, 8]

def solve():
  ans = 0

  heapq.heapify(l)
  for _ in range(0, n-1):
    v1 = heapq.heappop(l)
    v2 = heapq.heappop(l)
    ans += v1 + v2

    heapq.heappush(l, v1 + v2)

  return ans

print("{}".format(solve()))
