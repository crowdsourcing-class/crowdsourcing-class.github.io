---
layout: default
img: ML
caption: Crowdsourcing FTW!
title: Homework 4 | Playing with Classifire
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 24.</div>

Training a classifier<span class="text-muted"> : Assignment 4</span> 
=============================================================
In the remaining weekly homework assignments, the class will be working to build a large database of gun violence incidents across the country. As computer scientists, we often take for granted the large amounts of data that are available. Other fields, however, such as the social sciences, are often limited in their ability to carry out robust studies because of a lack of data. There is a lot of room for smart, creative people like yourselves to make big strides in computational approaches to social science disciplines like economics, sociology, political science, and public health. And even if it is just [dressed-up statistics](http://en.wikipedia.org/wiki/Data_science#Criticism), getting to use sexy names like "data science" and "machine learning" will make your mother proud.

We will be collecting data for our database from articles which are published in local newspapers across the country. We will use crowdsourcing to extract the structured information from these articles, but as a first step, we need to collect articles that describe incidences of gun violence. This is easier said than done. We can easily grab a handful of articles manually, but in order to build a meaningful database, we want to be able to gather data from a lot of articles, too many to do by hand. This is a picture perfect use of machine learning. If we can find a small number of examples of gun-related articles and of non-gun-related articles, we can train a model to predict for a million or more articles, with hopefully reasonable accuracy, which articles describe gun violence and which do not. 

We have already collected training data for you. Chris crawled a [NY Times blog about gun violence](http://nocera.blogs.nytimes.com/category/gun-report/) and gathered about 9,000 articles describing gun-related crimes. We are pulling examples of non-gun-related articles from a [local news corpus](ihttp://www.cs.jhu.edu/~anni/papers/alnc_lrec14.pdf) from Johns Hopkins.  In total you will have about 70K articles (~7 non-gun articles for every 1 gun article) to train your classifier. 

##To Do

Your task will be to build a classifier following our guidelines, and [respond to some questions about the process](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). After that, you are free to experiment. We have held out some secret data that we will use to test your classifiers. The student/s with the best performing classifier will be given $1,000,000! Or extra credit. Probably extra credit.

1. [Download the data](assignments/downloads/articles.gz) and unzip it with the Unix <code>gun</code>zip command. The data is in the format of one article per line. Each line has two values (tab separated): a label (0 for non-gun, 1 for gun), and the text of the article. 

2. [Download the code template](assignments/downloads/classifier_template.py) and look through the function stumps. These steps should seem familiar if you think back to Wednesday's lecture. Look especially closely at the functions flagged with "TODO." These are the ones you will edit.

3. The simplest way to build a classification algorithm is to used a rule based system. Look at the function rule_based_classifier(). This function doesn't bother itself with mathy mumbo jumbo, it just looks for keywords it thinks are indicative of gun-related articles. If one of the keywords appears, it predicts "1" (or "gun-related") and otherwise it picks "0". Right now we use just one keyword, "shooting." Try running the code and see how well this very simple method works.

	Now experiment with adding a few more keywords. See how high you can make the accuracy using this method. You will answer a few questions about this in the questionaire. 

4. You can get surprisingly far with a rule-based classifier in this setting. But why stop there? Why not use ALL THE KEYWORDS!? That is precisely what statistical models are for! 

	For the statistical model, your code will really just need to do one thing. That is, you need to build two side-by-side data structures: a *feature matrix* and a *label vector*. Your feature matrix will represent one article on each row, and each column will correspond to some "feature" you can observe about that article. The label vector will give the correct labels of each article, so that the nth element of the vector is 1 if the nth row of the matrix corresponse to a gun-related article.
	
	Look at the function get_features() in line 18. The template builds a stupid classifier whose feature matrix contains only one feature, which has the same value for every article. Try running it as follows and see that you get the below output. Here, the classifier is trying to make predictions, but has absolutely no information to work with. As a result, it just guesses based on the [prior probability](http://en.wikipedia.org/wiki/Prior_probability). I.e. this accuracy is the result of the classifier chosing the label "0" (or "non-gun-related") for every article.

	<pre><code> $ python classifier.py articles.txt 
	Fold 0 : 0.87449
	Fold 1 : 0.87624
	Fold 2 : 0.87687
	Fold 3 : 0.87456
	Fold 4 : 0.87526
	Test Average : 0.87548 </code></pre>

	Using your well-honed word-counting skills from bootcamp, try rewriting get_features() so that, for each article, the features are simply all of the words which are in that article. E.g. for the sentence "That guy shot that other guy," you will want a feature dictionary that looks like

	<pre><code> {'That' : 1, 'guy' : 2, 'shot' : 1, 'that' : 1, 'other' : 1}</code></pre>
	
	This is what is referred to in NLP as a "unigram features." 

	Try it and then record your experience in the [questionarie](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). For your classifier analysis, you need to look at feature weights that have been learned, and will need to see the predictions the classifier makes for individual articles. Look at the [functions available to you](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) through the LogisiticRegression classifier to get you started. 

And with that- Good luck! Start early and have fun! If robots are going to run the world, the need to first know the difference between articles about gun violence and articles about the weather. So go! Make it happen! 

Don't forget to answer all of the questions in the [questionaire](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form) when you are done, and to submit your final classifier code via turnin. 

<pre><code>$ turnin -c nets213 -p classifier -v classifier.py</code></pre>

Your code and questions are due <b>Wednesday, September 24</b>. You can work in pairs on this assignment.  You must declare the fact that you are working together when you turn in the questionaire.  If you are working with a partner, only one of you needs to turn in the code, but you must specify who will be turning it in on the questionaire. You cannot add or change partners after the code and questionaire are submitted.

Related Projects
================


* [Gun Violence Archive](http://gunviolencearchive.org)
* [Mass Shooting Tracker](http://shootingtracker.com/wiki/Main_Page)
* [Uniform Crime Reporting Statistics](http://www.ucrdatatool.gov/Search/Crime/State/StatebyState.cfm)
* [Police-shooting Database](http://regressing.deadspin.com/deadspin-police-shooting-database-update-were-still-go-1627414202) - [Gawker article](http://gawker.com/what-ive-learned-from-two-years-collecting-data-on-poli-1625472836), [NPR story](http://www.npr.org/2014/08/21/342228794/ferguson-turns-lens-on-police-involved-killings-but-some-facts-are-few)
* [Fatal Encounters](http://www.fatalencounters.org)
* [Rates of gun homicides by country compiled by The Guardian](http://www.theguardian.com/news/datablog/2012/jul/22/gun-homicides-ownership-world-list)
* [USA TODAY research reveals flaws in mass-killing data](http://www.usatoday.com/story/news/nation/2013/12/03/fbi-mass-killing-data-inaccurate/3666953/)