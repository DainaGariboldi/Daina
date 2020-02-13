N = int(input())
M = []
Sum = 0
String = input()
M = String.split()
M = list(map(int, M))
Largest = max(M)
Sum = sum(M)
print (Sum%Largest)