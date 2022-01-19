n = int(input())
data = []
for i in range(n):
    data.append([int(temp) for temp in input().split(" ")])

pos = [int(temp) for temp in input().split(" ")]
result = -1
for i in range(n-1, -1, -1):
    if data[i][0] + data[i][2] >= pos[0] >= data[i][0] and data[i][1] + data[i][3] >= pos[1] >= data[i][1]:
        result = i + 1
        break
print(result)
