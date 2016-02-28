import nltk
import pprint
try:
	import cPickle as pickle
except ImportError:
	import pickle

def get_data():
	f_filtered_data = open('all_reviews_filtered')
	all_reviews = []
	for i in range(2000):
		l = f_filtered_data.readline()
		words, label = l.split('\t')
		words = words.split()
		label = label.replace('\n','')
		all_reviews.append((words,label))
	return all_reviews

# print get_data()[:3]
def pickle_data(data):
	f = open('pickled_1_10000_reviews','wb')
	pickle.dump(data,f)
	f.close()
	return

if __name__ == '__main__':
	pickle_data(get_data())

