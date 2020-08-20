
n = int(input())
inf = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
	first = inf.pop(-1)
	for wrestler in inf:
		if first[0] < wrestler[0]:
			