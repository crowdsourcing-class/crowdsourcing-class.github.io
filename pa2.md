---
layout: default
img: ML
caption: Crowdsourcing FTW!
title: Homework 4 | Playing with classifier
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 24.</div>

Playing with classifier<span class="text-muted">: Assignment 4</span> 
=============================================================
Over the remaining assignments, we will be working, as a class, to build a large database of gun violence incidences across the country. As computer scientists, we often take for granted the large amounts of data that are available. Other fields, however, such as the social sciences, are often limited in their ability to carry out robust studies because of a lack of data. There is a lot of room for smart, creative people like yourselves to make big strides in computational social science disciplines, like economics, sociology, political science, and public health. And even if it is just [dressed-up statistics](http://en.wikipedia.org/wiki/Data_science#Criticism), getting to use sexy names like "data science" and "machine learning" will make your mother proud.

We will be collecting data for our database from articles which are published in local newpapers across the country. We will use crowdsourcing to extract the structured information from these articles, but as a first step, we need to collect articles that describe incidences of gun violence. This is easier said than done. We can easily grab a handful of articles manually, but in order to build a meaningful database, we want to be able to gather data from a lot of articles, too many to do by hand. This is a picture perfect use of machine learning. If we can find a small number of examples of gun-related articles and of non-gun-related articles, we can train a model to predict for a million or more articles, with hopefully reasonable accuracy, which articles describe gun violence and which do not. 

We have already collected training data for you. Chris crawled a [NY Times blog about gun violence](http://nocera.blogs.nytimes.com/category/gun-report/) and gathered about 10,000 articles describing gun-related crimes. We are pulling examples of non-gun-related articles from a [local news corpus](ihttp://www.cs.jhu.edu/~anni/papers/alnc_lrec14.pdf) from Johns Hopkins.  In total you will have about 110K articles (10 non-gun articles for every 1 gun article) to train your classifier. 

##To Do

Your task will be to build a classifier following our guidelines, and respond to some questions about the process [here](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). After that, you are free to experiment. We have held out some secret data that we will use to test your classifiers. The student/s with the best performing classifier will be given $1,000,000! Or extra credit. Probably extra credit.

1. Download the data [here](assignments/downloads/articles.gz) and unpack it. The data is in the format of one article per line. Each line has two values (tab separated): a label (0 for non-gun, 1 for gun), and the text of the article. 

2. Download the code template [here](assignments/downloads/classifier_template.py) and look through the function stumps. These steps should seem reasonable if you think back to Wednesday's lecture.

3. Your code will really just need to do one thing. That is, you need to build two side-by-side data structures: a *feature matrix* and a *label vector*. Your feature matrix will represent one article on each row, and each column will correspond to some "feature" you can observe about that article. The label vector will give the correct labels of each article, so that the nth element of the vector is a 1 if the nth row of the matrix corresponds to a gun-related article, and 0 otherwise. 
	
	The template builds a stupid classifier whose feature matrix contains only one feature, which has the same value for every article. Try running it as follows and see that you get the below output. Here, the classifier is trying to make predictions, but has absolutely no information to work with. As a result, it just guesses based on the [prior probability](http://en.wikipedia.org/wiki/Prior_probability). I.e. this accuracy is the result of the classifier chosing the label "0" (or "non-gun-related") for every article.

	<pre><code> $ python classifier.py articles.txt 
	Fold 0 : 0.88937
	Fold 1 : 0.88818
	Fold 2 : 0.88752
	Fold 3 : 0.88471
	Fold 4 : 0.88531
	Train Average : 0.88654
	Test Average : 0.88702 </code></pre>

4. Obviously we want to do better than choosing the same label for every article. Look at the function get_features() in line 18. This is where we are building up a list of features and their values for each article. One intuitive thing we can think of doing is adding some key words that we think might be very indicative of gun-violence articles. Try adding a boolean feature which is true if the article contains the word "shooting" and false otherwise. What is your performance now?

5. Try adding another few keywords and checking the classifier performance. Try adding all of the keyword features together, and then answer Part 1 of the [questionaire](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). 

6. You can get surprisingly far with keywords. So why not just use ALL THE KEYWORDS!? Using your well-honed word-counting skills from bootcamp, try rewriting get_features() so that, for each article, the features are simply all of the words which are in that article. E.g. for the sentence "That guy shot that other guy," you will want a feature dictionary that looks like

	<pre><code> {'That' : 1, 'guy' : 1, 'shot' : 1, 'that' : 1, 'other' : 1, 'guy' : 1}</code></pre>
	
	This is what is referred to in NLP as a "unigram features." 

	Try it, run it, and answer Part 2 in the [questionarie](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form).

	To do your classifier analysis, you will probably need to write some more functions. E.g., you will need to look at some probabilities that have been learned, and will need to see the label the classifier chooses for individual articles. Look at the [functions available to you](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) through the MultinomialNaiveBayes classifier to get you started. 

7. And now is the fun! The unigram model does pretty well. But can you do better? Here are some things to consider:

	- We talked after the bootcamp about how capitalization and punctuation can cause counter-intuitive results. Can you fix these and improve performance? 
	- We also talked about stopwords last week. How might these confuse Naive Bayes? Keep in mind that you can [look at which features have high conditional probabilities](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) after you have trained the model.
	- Can you do better than a simple binary feature? What about frequencies of words in an article? Are all words created equal or are [some more important than others](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)?
	- Naive Bayes is...naive. There are lots of other models you can try, which all have different strengths and weaknesses.
	- No one said you have to split the articles into single word phrases. If unigrams are good, then [bigrams](http://en.wikipedia.org/wiki/N-gram) must be two times better! Be careful of [overfitting](http://en.wikipedia.org/wiki/Overfitting), though...

And with that- Good luck! Start early and think big! If robots are going to run the world, the need to first know the difference between articles about gun violence and articles about the weather. So go! Make it happen!


