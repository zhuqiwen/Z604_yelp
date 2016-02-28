import nltk
import pprint
try:
	import cPickle as pickle
except ImportError:
	import pickle

pickled_file = raw_input('give me the pickled file: \n')
#pickled_file = '/N/u/qiwzhu/Karst/z604_yelp/review/pickled_1_10000_reviews'
def read_pickled_reviews(pickled_file):
	f = open(pickled_file,'rb')
	data = pickle.load(f)
	f.close()
	return data

# pprint.pprint(read_pickled_reviews()[-1])

def get_words_in_data(data):
	all_words = []
	for words, label in data:
		all_words.extend(words)
	return all_words


def get_word_features(all_words):
	word_freq = nltk.FreqDist(all_words)
	top_n = 20000
	start_index = 0
#	word_freq = sorted(word_freq.items(), key = lambda x:x[1], reverse = True)[:top_n]
#	word_freq = {i[0]:word_freq.index(i)+start_index for i in word_freq}
	word_freq = word_freq.items()[:top_n]
	word_freq = {i[0]:i[1] for i in word_freq}
	word_features = word_freq.keys()
	return word_features


def extract_features(doc):
	doc_words = set(doc) # get all words unrepeatedly in doc, a doc is a list of words in review.
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in doc_words)
	return features


data  = read_pickled_reviews(pickled_file)
all_words = get_words_in_data(data)
word_features = get_word_features(all_words)
# pprint.pprint(get_word_features(all_words))

# *********************************
featuresets = [(extract_features(doc),c) for (doc,c) in data]

n = int(len(featuresets) * 0.9)
train_set, test_set = featuresets[:n], featuresets[n:]

my_nb_clfier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(my_nb_clfier,test_set)




# **********************************





# reviews_4_training = data[:len(data)-(len(data)/10)]
# # print len(reviews_training)

# reviews_4_test = data[len(data)-(len(data)/10):]
# # print len(reviews_4_test)
# training_set = nltk.classify.apply_features(extract_features, reviews_4_training)
# pprint.pprint(training_set)
# # 
# # # print my_nb_clfier.show_most_informative_features(50)
# # # print help(my_nb_clfier)

# # for t in reviews_4_test:
# # 	review, label = t
# # 	review = extract_features(review)
