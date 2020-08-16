class Solution:
	def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
		# letter로 안되는 애들 뺌.
		for word_i in words:
			word_list = list(word_i)
			for word in word_list:
				if word in letters:
					pass
				else:
					print(word_i)
					words.remove(word_i)

		# 문자 스코어 딕트로 연결
		score_true = {}
		for i in range(len(score)):
			if score[i] != 0:
				score_true[chr(97 + i)] = score[i]

		# 가장 높은점수를 구해야함. - 점수를 구해보자.
		sum_score = {}
		for word in words:
			word_list: list = word
			for word_i in word_list:
				try:
					sum_score[word] += score_true[word_i]
				except KeyError:
					sum_score[word] = score_true[word_i]

		# 가장 높은것 부터 차례로 해보자
		max_word_score = max(sum_score.values())
		# max_word = str([word for word, score in sum_score.items() if score == max_word])

		return sum_score



# 다른사람 풀이
class Solution2():
	def maxScoreWords(self, words, letters, score):
		self.max_score = 0
		words_score = [sum(score[ord(c) - ord('a')] for c in word) for word in words]
		words_counter = [collections.Counter(word) for word in words]

		def dfs(i, curr_score, counter):
			if curr_score + sum(words_score[i:]) <= self.max_score:
				return
			self.max_score = max(self.max_score, curr_score)
			for j, wcnt in enumerate(words_counter[i:], i):
				if all(n <= counter.get(c, 0) for c, n in wcnt.items()):
					dfs(j + 1, curr_score + words_score[j], counter - wcnt)

		dfs(0, 0, collections.Counter(letters))
		return self.max_score