def get_most_freq_word(sentence):
	

	s=sentence.split(" ")


	word_count={}
	for word in s:
		if word in word_count.keys():
			word_count[word]+=1
		else:
			word_count[word]=1
	freq_words=[]
	for word in word_count.keys():
		if word_count[word]==max(word_count.values()):
			freq_words.append(word)

	print("Most frequent word (first in alphabetical order): {}".format(sorted(freq_words)[0]))
			

	#print(word_count)

get_most_freq_word("A cat cat bat bat is an animal cat")
get_most_freq_word("A cat cat bat bat is an animal cat bat")

