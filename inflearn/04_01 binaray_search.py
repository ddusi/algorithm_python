import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
Num: list = list(map(int, input().split()))


def function(M, Num):
	Num.sort()
	return Num.index(M) + 1


print(function(M, Num))
