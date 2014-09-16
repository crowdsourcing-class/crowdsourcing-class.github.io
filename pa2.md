---
layout: default
img: python
caption: Hello world!
title: Homework 4 | Calling the shots
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 24.</div>

Calling the shots<span class="text-muted">: Assignment 4</span> 
=============================================================
Over the remaining assignments, we will be working, as a class, to build a large scale database of gun violence across the country. As computer scientists, we often take for granted the large amounts of data that are available. Other fields, however, such as the social sciences, are often limited in their ability to carry out robust studies because of a lack of data. There is a lot of room for smart, creative people like yourselves to make big strides in computational social sciences, like economics, sociology, political science, and public health. There's even a [sexy name](http://en.wikipedia.org/wiki/Data_science) for the field, and a Venn Diagramm to boot. So you can make your mom proud.

We will be collecting data for our data base from articles which are published in local newpapers across the country. We will use crowdsourcing to extract the structured information from these articles, but as a first step, we need to collect articles that describe incidences of gun violence. This is easier said than done. We can easy grab a handful of articles manually, but in order to build a meaningful database, we want to be able to gather data from a lot of data bases. This is a picture perfect use of machine learning. If we can find small number of examples of gun-related articles and of non-gun-related articles, we can train a model to predict, with hopefully reasonable accuracy, which articles describe gun violence and which do not. 

As training data, Chris crawled a [NY Times blog about gun violence](http://nocera.blogs.nytimes.com/category/gun-report/) and gathered about 10,000 articles describing gun-related crimes. We are pulling examples of non-gun-related articles from a [local news corpus](ihttp://www.cs.jhu.edu/~anni/papers/alnc_lrec14.pdf) from Johns Hopkins.  In total you will have about 110K articles (10 non-gun articles for every 1 gun article) to train your classifier. 

##To Do

Your task will be to build a classifier following our guidelines, and respond to some questions about the process [here](). After that, you are free to experiment. We have held out some secret data that we will use to test your classifiers, so the student/s with the best performing classifier will be given $1,000,000! Or extra credit. Probably extra credit.

1. Download the data [here]() and unpack it. The data is in the format of one article per line. Each line has two values (tab separated): a label (0 for non-gun, 1 for gun), and the text of the article. 

2. Download the code template [here]() and look through the function stumps. These steps should seem reasonable if you think back to Wednesday's lecture.

3. Your code will really just need to do one thing. That is, you need to build two side-by-side data structures: a *feature matrix* and a *label vector*. Your feature matrix will represent one article on each row, and each column will correspond to some "feature" you can observe about that article. The label vector will give the correct labels of each article, so that the first element of the vector is a 1 if the first row of the matrix corresponds to a gun-related article, and 0 otherwise. The template builds a stupid classifier whose feature matrix contains only one feature, which has the same value for every article. Try running it as follows and see that you get the below output. This is the result of the classifier chosing the label "0" or "non-gun-related" for every article.

	<pre><code> $ python classifier.py articles.txt 
	Fold 0 : 0.88937
	Fold 1 : 0.88818
	Fold 2 : 0.88752
	Fold 3 : 0.88471
	Fold 4 : 0.88531
	Train Average : 0.88654
	Test Average : 0.88702 </code></pre>

4. Obviously we want to do better than choosing the same label for every article. Look at the function get_features() in line 18. This is where we are building up a list of features and their values for each article. One intuitive thing we can think of doing is adding some key words that we think might be very indicative of gun-violence articles. Try adding a boolean feature which is true if the article contains the word "shooting" and false otherwise. What is your performance now?

5. Try adding another 4 or 5 keywords and checking the classifier performance. Once you have done this, answer the first XXX questions in the [questionaire](). 

6. 


