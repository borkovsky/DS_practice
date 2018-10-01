# # # Sock Mercant
# from https://www.hackerrank.com/challenges/sock-merchant/problem

socks = [1,1,1,2,2,2,2,3,3,3,3,3,3,3,4]

from collections import Counter

def sock_pairs(socks):
  pairs = 0
  pairless = 0
  c = Counter(socks)
  print(c)
  for i in c:
    if c[i] < 2:
      pairless += 1
    else:
      pairs += (c[i] // 2)
  return pairs, pairless

print(sock_pairs(socks))
