import sys

## 1차 시도
# sys.stdin = open("input.txt", "r")
#
#
# def Count(capacity):
# 	cnt = 1
# 	sum = 0
# 	for x in music:
# 		if sum + x > capacity:
# 			cnt += 1
# 			sum = x
# 		else:
# 			sum += x
# 	return cnt
#
#
# n, m = map(int, input().split())
# music = list(map(int, input().split()))
#
# lt: int = 1
# rt: int = sum(music)
# res: int = 0
#
# while lt <= rt:
# 	print("rt = ", rt)
# 	mid = (lt + rt) // 2
# 	print(mid)
# 	if Count(mid) <= m:
# 		res = mid
# 		rt = mid - 1
# 	else:
# 		lt = mid + 1
#
# print(res)


# #
# # num_sum_len: int = sum(num) // m
# # result: int = 0
# # for i in num:
# # 	result += i
# # 	if i ==
#
#
# n, m = map(int, input().split())
# music = list(map(int, input().split()))
#
# lt: int = 1
# rt: int = sum(music)
#
# mid: int = (lt + rt) // 2
#
#
# def Count(capacity):
# 	cnt = 0
# 	num_sum = 0
# 	for music_times in music:
# 		if num_sum > mid:
# 			cnt += 1
# 			num_sum = music_times
# 		elif num_sum == mid:
# 			cnt += 1
# 			num_sum = 0
# 		else:
# 			num_sum += music_times
# 	return cnt + 1
#
#
# result: list = []
# while mid > 0:
# 	if Count(mid) == m:
# 		result.append(mid)
# 		mid = mid - 1
# 	else:
# 		mid = mid - 1
#
# print(min(result))
#


### 3차시도 ( 답지 )
'''
n, m = map(int, input().split())
music = list(map(int, input().split()))

lt: int = 1
rt: int = sum(music)


def Count(capacity):
	cnt: int = 1
	sum: int = 0

	for i in music:
		if sum + i > capacity:
			cnt += 1
			sum = i
		else:
			sum += i
	return cnt


# 이분탐색 시작.
result: int = 0
maxx = max(music)
while lt <= rt:
	mid: int = (lt + rt) // 2
	if mid>=maxx and Count(mid) <= m:
		result = mid
		rt = mid - 1
	else:
		lt = mid + 1

print(result)
'''

### 4차 시도
n, m = map(int, input().split())
music = list(map(int, input().split()))


def Count(capecity):
	sum: int = 0
	cnt: int = 1
	for i in music:
		if sum + i > capecity:
			cnt += 1
			sum = i
		else:
			sum += i
	return cnt


lt: int = 1
rt: int = sum(music)
result: list = []

while lt <= rt:
	mid: int = (lt + rt) // 2
	if Count(mid) <= m:
		rt = mid - 1
		result.append(mid)
	else:
		lt = mid + 1
print(min(result))
