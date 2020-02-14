N = int(input())
m = []
Inp = input()
for x in range(N):
  m = [int(i) for i in Inp.split()]
Small = min(m)
Bigg = max(m)
print(Bigg - Small)