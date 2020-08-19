import sys


# sys.stdin = open("input.txt", "r")

def Count(len):
	cnt = 1
	ep = line[0]
	for i in range(1, n):
		if line[i] - ep >= len:
			cnt += 1
			ep = line[i]
	return cnt


n, c = map(int, (input().split()))
line = [int(input()) for i in range(n)]
line.sort()

lt: int = 1
rt: int = max(line)
result: list = []

while lt <= rt:
	mid = (lt + rt) // 2
	if Count(mid) >= c:
		res = mid
		lt = mid + 1
	else:
		rt = mid - 1
print(res)
