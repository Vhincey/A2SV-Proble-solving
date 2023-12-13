t = int(input()) 
result = []
 
def diagonal_sum(chessboard, n, m):
    max_sum = 0
    for i in range(n):
        for j in range(m):
            sum = chessboard[i][j]
            x, y = i-1, j-1
            while x >= 0 and y >= 0:
                sum += chessboard[x][y]
                x -= 1
                y -= 1
            
            x, y = i-1, j+1
            while x >= 0 and y < m:
                sum += chessboard[x][y]
                x -= 1
                y += 1
            
            x, y = i+1, j-1
            while x < n and y >= 0:
                sum += chessboard[x][y]
                x += 1
                y -= 1
            
            x, y = i+1, j+1
            while x < n and y < m:
                sum += chessboard[x][y]
                x += 1
                y += 1
            
            max_sum = max(max_sum, sum)
    
    return max_sum
 
for _ in range(t):
    n, m = map(int, input().split())
    chessboard = [list(map(int, input().split())) for _ in range(n)]
    max_sum = diagonal_sum(chessboard, n, m)
    result.append(max_sum)
 
for res in result:
    print(res)
