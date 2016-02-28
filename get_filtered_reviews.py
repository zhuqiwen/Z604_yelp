import string


f = open('all_reviews')
f_out = open('all_reviews_filtered','w')
for l in f:	
	words, sentiment = l.split('\t')
	for p in string.punctuation:
		words = words.replace(p, '')
	words_filtered = [w.lower() for w in words.split() if len(w) >= 3]
	f_out.write(' '.join(w for w in words_filtered)+'\t'+sentiment)

f.close()
f_out.close()