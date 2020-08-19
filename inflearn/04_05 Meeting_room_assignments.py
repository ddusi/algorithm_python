import sys

# sys.stdin = open("input.txt", "r")

n: int = int(input())
books = [list(map(int, input().split())) for i in range(n)]
result: list = []
books.sort()


def Count(first):
	cnt: int = 1
	k: int = 1
	meeting: list = first
	for i in range(k, n):
		if int(meeting[1]) <= int(books[i][0]):
			cnt += 1
			gap: list = []
			for j in range(i, n):
				gap.append([(books[j][1] - books[j][0]) + (books[j][0] - books[i][0]), books[j]])
				gap.sort()
			meeting = gap[0][1]
			k = gap[0][1][1]
	return cnt


for book in books:
	result.append(Count(book))

print(max(result))
