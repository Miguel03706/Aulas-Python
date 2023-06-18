# input1 = input().split()
# n = int(input1[0])
# m = int(input1[1])
# s = int(input())

# sensores = []
# for sensor in range(s):
# 	input2 = input().split()

# 	sensores.append({
# 		"x":int(input2[0])-1,
# 		"y":int(input2[1])-1,
# 		"r":int(input2[2]),
# 		})



# dimensao_x = [0 for _ in range(m+5)] # m = x
# mapa = [dimensao_x.copy() for _ in range(n+5)] # n = y


# for sensor in sensores:
# 	x = sensor["x"]
# 	y = sensor["y"]
# 	r = sensor["r"]

# 	X_min = x-r
# 	if (X_min<0):
# 		X_min = 0
		
# 	X_max = x+r


# 	Y_min = y-r
# 	if (Y_min<0):
# 		Y_min = 0

# 	Y_max = y+r

# 	for i in range(X_min,X_max+1):
# 		for j in range(Y_min, Y_max+1):
# 			if(i >= 0 and i <= m and j >= 0 and j <= n):
# 				mapa[i][j] += 1


# soma = 0
# for i in mapa:
# 	for x in i:
# 	    soma+=x


# print(int(soma/(n*m)-1))

N, M = map(int, input().split())
S = int(input())

sensores = []
for _ in range(S):
    X, Y, R = map(int, input().split())
    sensores.append((X, Y, R))

total_sensores = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        num_sensores = 0
        for sensor in sensores:
            X, Y, R = sensor
            if abs(X - i) <= R and abs(Y - j) <= R:
                num_sensores += 1
        total_sensores += num_sensores

A = total_sensores / (N * M)
Z = int(A)
print(Z)
