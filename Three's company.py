N = int(input())
Inp = str(input())
L = list(Inp)
M = []
for i in range (0, len(L)):
    M.append(L[i]*3)
F = ""
F = F.join(M)
print (F)