#!/bin/python

import sys
import random
import operator
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
import nltk

#read in raw data from file and return a list of (label, article) tuples
def get_data(filename): return [line.strip().split('\t') for line in open(filename).readlines()]

#this is the main function you care about; pack all the cleverest features you can think of into here.
def get_features(X) : 
	features = []
	for x in X : 
		f = {}
		f['useless feature'] =  1.0
		features.append(f)
	return features

#vectorize feature dictionaries and return feature and label matricies
def get_matricies(data) : 
	dv = DictVectorizer()
	le = LabelEncoder()
	y = [d[0] for d in data]
	X = get_features([d[1] for d in data])
	return le.fit_transform(y), dv.fit_transform(X)

#train and multinomial naive bayes classifier
def train_classifier(X, y):
	clf = MultinomialNB()
	clf.fit(X,y)
	return clf 

#test the classifier
def test_classifier(clf, X, y):
	return clf.score(X,y)

#cross validation	
def cross_validate(X, y, numfolds=5):
	train_accs = []
	test_accs = []
	split = 1.0 / numfolds
	for i in range(numfolds):
		x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=i)
		clf = train_classifier(x_train, y_train)
		train_acc = test_classifier(clf, x_train, y_train)
		train_accs.append(train_acc)
		test_acc = test_classifier(clf, x_test, y_test)
		test_accs.append(test_acc)
		print 'Fold %d : %.05f'%(i,test_acc)
	train_average = float(sum(train_accs))/ numfolds
	test_average = float(sum(test_accs))/ numfolds
	#How does the training accuracy compare to the accuracy on the test data? Why?
	print 'Train Average : %.05f'%(train_average)
	print 'Test Average : %.05f'%(test_average)
	print
	return train_average, test_average


if __name__ == '__main__' : 

	raw_data = get_data(sys.argv[1])
	y, X = get_matricies(raw_data)
	cross_validate(X,y)

