n, m = map(int, input().split())
k = int(input())

board = []
bombs = []

for x in range(n):
    board.append([])
    for y in range(m):
        board[x].append(0)

for _ in range(k):
    x, y = map(int, input().split())
    bombs.append((x - 1, y - 1))
    board[x - 1][y - 1] = '*'

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            continue
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ni = i + dx
                nj = j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == '*':
                        count += 1
        board[i][j] = str(count)

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            print('*', end=' ')
        else:
            print(board[i][j], end=' ')
    print()