n = int(input())
 
for i in range(n):
    s = input()
 
    res = set()
 
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            res.add(s[i])
            i += 1
 
    sorted_res = sorted(res)
    print(''.join(sorted_res))
