t = int(input())

for v in range(t):
    n, c = map(str, input().split())
    s = list(input())
    n = int(n)
    s += s
    
    count = 0
    maxi = 0
    flag = False
    
    for i in range(len(s)):
        if s[i] == c:
            flag = True
        if s[i] == 'g':
            flag = False
            maxi = max(maxi, count)
            count = 0
        if flag:
            count += 1
            
    print(maxi)
