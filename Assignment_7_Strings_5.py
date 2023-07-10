def revAlternateK(s, k):
	i = 0
	
	while(i < len(s)):

		if (i + k > len(s)):
			break
		ss = s[i:i + k]
		s = s[:i]+ss[::-1]+s[i + k:]
		
		i += 2 * k
	
	return s


s = "abcdefg"
k = 2
print(revAlternateK(s, k))
