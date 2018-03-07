# This is Work in progress, since the code has not been tested yet.


def nearly_equal(str1, str2):
    """Count the # of differences between equal length strings str1 and str2"""
    word_len = len(str1)
    words_list = []
    word = word1
    start = ord("a")
    end = ord("z") + 1
    for i in range(word_len):
        if i < word_len - 1:
	        words_list.append(word[:i] + word[i + 1] + word[i] + word[i + 2:])
		for x in range(start, end):
			x = chr(x)
            words_list.append(word[:i] + x + word[i:])
            words_list.append(word[:i] + word[i + 1:])
            words_list.append(word[:i] + x + word[i + 1:])
	if str2 in words_list:
		return True
	else:
		return False
            
if __name__ == "__main__":
    import sys
    nearly_equal(sys.argv[1],sys.argv[2])
