print("Enter the initial weights: ")
w = list(map(int, input().split()))
N = [[0, 0, 0]]
P = [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# N1 [1,0,0,0]
# P1 [1,0,0,1], P2 [1,0,1,0], P3 [1,0,1,1], P4 [1,1,0,0], P5 [1,1,0,1], P6[1,1,1,0] , P7[1, 1, 1, 1]
# # W=[0,0,-1,2]
while True:
    temp = w[:]
    for x in N:
        sum = 0
        for y in range(len(x)):
            sum += temp[y]*x[y]
        if sum >= 0:
            for y in range(len(temp)):
                temp[y] -= x[y]
    for x in P:
        sum = 0
        for y in range(len(x)):
            sum += temp[y]*x[y]
        if sum < 0:
            for y in range(len(temp)):
                temp[y] += x[y]
    if temp == w:
        break
    w = temp[:]
print(w)