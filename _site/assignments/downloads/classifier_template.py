#!/bin/python

import sys
import random
import operator
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split

#read in raw data from file and return a list of (label, article) tuples
def get_data(filename): 
	data = [line.strip().split('\t') for line in open(filename).readlines()]
	random.shuffle(data)
	return data

#this is the main function you care about; pack all the cleverest features you can think of into here.
def get_features(X) : 
	features = []
	for x in X : 
		f = {}
		#TODO replace this dummy feature function with a unigram model, like we did in class
		f['useless feature'] =  1.0
		features.append(f)
	return features

#vectorize feature dictionaries and return feature and label matricies
def get_matricies(data) : 
	dv = DictVectorizer(sparse=True) 
	le = LabelEncoder()
	y = [d[0] for d in data]
	texts = [d[1] for d in data]
	X = get_features(texts)
	#Here we are returning 5 things, the label vector y and feature matrix X, but also the texts from which the features were extracted and the 
	#objects that were used to encode them. These will come in handy for your analysis, but you can ignore them for the initial parts of the assignment
	return le.fit_transform(y), dv.fit_transform(X), texts, dv, le

#train and multinomial naive bayes classifier
def train_classifier(X, y):
	clf = LogisticRegression()
	clf.fit(X,y)
	return clf 

#test the classifier
def test_classifier(clf, X, y):
	return clf.score(X,y)

#cross validation	
def cross_validate(X, y, numfolds=5):
	test_accs = []
	split = 1.0 / numfolds
	for i in range(numfolds):
		x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=i)
		clf = train_classifier(x_train, y_train)
		test_acc = test_classifier(clf, x_test, y_test)
		test_accs.append(test_acc)
		print 'Fold %d : %.05f'%(i,test_acc)
	test_average = float(sum(test_accs))/ numfolds
	print 'Test Average : %.05f'%(test_average)
	print
	return test_average

#run a rule based classifier and calculate the accuracy
def rule_based_classifier(data):
	correct = 0.0; total = 0.0
	for label, text in data : 
		prediction = '0'
		#TODO add more keywords, see how well they do alone and in combination
		if "shooting" in text : prediction = '1'
		if prediction == label : correct += 1
		total += 1
	print 'Rule-based classifier accuracy: %.05f'%(correct / total)

#train and multinomial naive bayes classifier
def get_top_features(X, y, dv):
	clf = train_classifier(X, y)
	#the DictVectorizer object remembers which column number corresponds to which feature, and return the feature names in the correct order
	feature_names = dv.get_feature_names() 

	#TODO: You will have to write code here to get the weights from the classifier, and print out the weights of the features you are interested in

def get_misclassified_examples(y, X, texts) :
	x_train, x_test, y_train, y_test, train_texts, test_texts = train_test_split(X, y, texts)
	clf = train_classifier(x_train, y_train)

	#TODO: You will have to write some code to call your classifier on each of the test examples, and check whether its prediction was right or wrong


if __name__ == '__main__' : 

	raw_data = get_data(sys.argv[1])
	
	print '\nRule-based classification'
	rule_based_classifier(raw_data)

	print '\nStatistical classification'
	y, X, texts, dv, le = get_matricies(raw_data)
	cross_validate(X,y)

#	get_top_features(X, y, dv)
#	get_misclassified_examples(y, X, texts)

