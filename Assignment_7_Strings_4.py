def reverseWords(string):
	st = list()

	for i in range(len(string)):
		if string[i] != " ":
			st.append(string[i])
		else:
			while len(st) > 0:
				print(st[-1], end="")
				st.pop()
			print(end=" ")

	while len(st) > 0:
		print(st[-1], end="")
		st.pop()


s = "Let's take LeetCode contest"
print(reverseWords(s))
