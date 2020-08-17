import sys

sys.stdin = open("input.txt", "r")

k, n = map(int, (input().split()))
num = [int(input()) for i in range(k)]

num_sum: int = sum(num)
num_max_len: int = num_sum // n

while True:
	result: int = 0
	for i in num:
		result += i // num_max_len
	if result == n:
		print(num_max_len)
		break
	else:
		num_max_len -= 1