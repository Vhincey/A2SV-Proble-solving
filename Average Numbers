N = int(input())
 
seq = list(map(int, input().split()))
 
Sum = sum(seq)
 
indices = []
for i in range(N):
    if seq[i] == (Sum - seq[i]) / (N - 1):
        indices.append(i + 1) 
        
 
if len(indices) == 0:
    print(0)
else:
    print(len(indices))
    print(*indices)
        
