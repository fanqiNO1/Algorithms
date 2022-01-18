def solve():
    data = input().split()

    rows = int(data[0])
    cols = int(data[1])
    horse_x = int(data[2])
    horse_y = int(data[3])
    horse_reached = horse_reach(horse_x, horse_y)

    board = [[0 for i in range(cols+1)] for j in range(rows+1)]
    board[0][0] = 1

    for i in range(rows+1):
        for j in range(cols+1):
            if (i, j) in horse_reached:
                board[i][j] = 0
            else:
                if j == 0 and i == 0:
                    continue
                elif j == 0:
                    board[i][j] = board[i-1][j]
                elif i == 0:
                    board[i][j] = board[i][j-1]
                else:
                    board[i][j] = board[i-1][j] + board[i][j-1]

    print(board[rows][cols])


def horse_reach(horse_x, horse_y):
    horse_reached = []
    horse_reached.append((horse_x, horse_y))
    horse_reached.append((horse_x - 2, horse_y - 1))
    horse_reached.append((horse_x - 2, horse_y + 1))
    horse_reached.append((horse_x - 1, horse_y - 2))
    horse_reached.append((horse_x - 1, horse_y + 2))
    horse_reached.append((horse_x + 2, horse_y - 1))
    horse_reached.append((horse_x + 2, horse_y + 1))
    horse_reached.append((horse_x + 1, horse_y - 2))
    horse_reached.append((horse_x + 1, horse_y + 2))
    return horse_reached


if __name__ == '__main__':
    solve()
