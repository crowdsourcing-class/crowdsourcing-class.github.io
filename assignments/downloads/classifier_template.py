#!/bin/python

import os
import sys
import string
import random
import operator
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO  

#read in raw data from file and return a list of (label, article) tuples
def get_data(filename): 
	data = [line.strip().split('\t') for line in open(filename).readlines()]
	random.shuffle(data)
	return data

#this function builds the feature matrix for the Decision Tree.
def get_dtree_features(X) :
	features = []
	#TODO : Add the features you would like to use to train the Decision Tree here.
	feature_list = ['gun']
	for x in X :
		f = {}
		for w in [word.strip(string.punctuation) for word in x.split()] :
			if w in feature_list : 
				f[w] = 1.0
		features.append(f)
	return features


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
def get_matricies(data, typ="unigram") : 
	dv = DictVectorizer(sparse=True) 
	le = LabelEncoder()
	y = [d[0] for d in data]
	texts = [d[1] for d in data]
	if typ == "tree":
		X = get_dtree_features(texts)
	else :
		X = get_features(texts)
	#Here we are returning 5 things, the label vector y and feature matrix X, but also the texts from which the features were extracted and the 
	#objects that were used to encode them. These will come in handy for your analysis, but you can ignore them for the initial parts of the assignment
	return le.fit_transform(y), dv.fit_transform(X), texts, dv, le

#train and multinomial naive bayes classifier
def train_classifier(X, y):
	clf = LogisticRegression()
	clf.fit(X,y)
	return clf 

#train a Decision Tree classifier
def train_dtree_classifier(X, y):
	clf = DecisionTreeClassifier(max_depth=None)
	clf.fit(X,y)
	return clf

#test the classifier
def test_classifier(clf, X, y):
	return clf.score(X,y)

#cross validation	
def cross_validate(X, y, dv=None, typ="unigram", numfolds=5,):
	test_accs = []
	split = 1.0 / numfolds
	for i in range(numfolds):
		x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=i)
		if typ == "tree" :
			clf = train_dtree_classifier(x_train, y_train)
		else :
			clf = train_classifier(x_train, y_train)
		test_acc = test_classifier(clf, x_test, y_test)
		test_accs.append(test_acc)
		print 'Fold %d : %.05f'%(i,test_acc)
	test_average = float(sum(test_accs))/ numfolds
	if typ == "tree" :
		with open("output.dot", 'w') as f:
			f = export_graphviz(clf, out_file=f, feature_names=dv.get_feature_names(), class_names=['Non Gun Related','Gun Related'])
		create_graph("decision-tree.png")
	print 'Test Average : %.05f'%(test_average)
	print
	return test_average

#run a rule based classifier and calculate the accuracy
def rule_based_classifier(data):
	correct = 0.0; total = 0.0
	for label, text in data : 
		prediction = '0'
		#TODO add more keywords, see how well they do alone and in combination
		if "gun" in text : prediction = '1'
		if prediction == label : correct += 1
		total += 1
	print 'Rule-based classifier accuracy: %.05f'%(correct / total)

#Extra Credit Rule Based Classifier
def extra_credit_classifier(data):
	correct = 0.0; total = 0.0
	for label, text in data : 
		prediction = '0'
		#TODO develop your conditional statements here
		if "shooting" in text : prediction = '1'
		if prediction == label : correct += 1
		total += 1
	print 'Reverse Engineered classifier accuracy: %.05f'%(correct / total)

#train and multinomial naive bayes classifier
def get_top_features(X, y, dv):
	clf = train_classifier(X, y)
	#the DictVectorizer object remembers which column number corresponds to which feature, and return the feature names in the correct order
	feature_names = dv.get_feature_names() 

	#The below code will get the weights from the classifier, and print out the weights of the features you are interested in
	features = [] #this will be a list of (feature_idx, weight) tuples
	for i,w in enumerate(clf.coef_[0]): 
		features.append((i,w))
	#Sort the list by values, with the largest ones first
	features = sorted(features, key=lambda e: e[1], reverse=True)

        #Print out the feature names and thier weights
	for i,w in features:
	  print '%s\t%s'%(feature_names[i], w)

def get_misclassified_examples(y, X, texts) :
	x_train, x_test, y_train, y_test, train_texts, test_texts = train_test_split(X, y, texts)
	clf = train_classifier(x_train, y_train)

	#TODO: You will have to write some code to call your classifier on each of the test examples, and check whether its prediction was right or wrong

def create_graph(file_name) :
	os.system("dot -Tpng output.dot -o " + file_name)
	os.unlink("output.dot")

if __name__ == '__main__' : 

	raw_data = get_data(sys.argv[1])
	
	print '\nRule-based classification'
	rule_based_classifier(raw_data)

################ Decision Tree ################

#	print '\nDecision Tree classification'
#	y, X, texts, dv, le = get_matricies(raw_data, "tree")
#	cross_validate(X,y,dv,"tree")

################ Statistical Classification ################
	print '\nStatistical classification'
	y, X, texts, dv, le = get_matricies(raw_data)
	cross_validate(X,y)

#	get_top_features(X, y, dv)
#	get_misclassified_examples(y, X, texts)

