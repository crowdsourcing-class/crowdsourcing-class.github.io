---
layout: default
img: big-data-for-dummies
caption: 
title: Homework 8 | Classification
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, November 13th.
</div>


Classification <span class="text-muted">: Assignment 8</span> 
=============================================================
Okay! This is it! The assignment you have all been waiting for! We will finally take all the data you guys gathered and do something with it (besides sit and marvel at 'look what my Turkers did!') The goal of this assignment is very straightforward: you want to predict the sentiment of each tweet using statistical machine learning. How you do it is almost entirely up to you. You will have two weeks (almost) to do this assignment, so use all the extra time to make your classifier as good as possible. These kinds of projects take a lot of finessing to get right. 

Because that warm feeling of personal satisfaction for having worked hard and done well only takes you so far, you guys will be competing to turn in the best classifier. I will collect some super secret test data that none of you will get to see, and whoever's classifier performs best will be given some awesome reward not yet known. Or maybe whoever performs worst will be publicly humiliated. We haven't decided which way to do it yet, but the point is, you want your classifier to do well. 

The following steps with help get you familiar with the data, get familiar with the code, and lay down a baseline classifier accuracy. Then you are free to go forth and do! Make us proud!

1. Sorry, one more thing to download. [scikit learn](http://scikit-learn.org/stable/) is an *awesome* python toolkit that takes all the hard things in machine learning and makes them trivially easy for us to use. (You should take Lyle Ungar's machine learning class, which will make you implement these algorithms in Matlab or R something else god awful, and then go back to working with scikit. It will be the most satisfying experience you will ever have as a programmer.) Instructions for installing it are [here](http://scikit-learn.org/stable/install.html). If you can use git, I recommend installing that way since it is fast and easy and lets you see the source code if you want to. 

	$ git clone git://github.com/scikit-learn/scikit-learn.git
	$ cd scikit-learn
	$ python setup.py install

    Installing packages has proven to be a huge pain in the ass in previous assignments. Try to get this installed ASAP so I can help you if there are problems. I actually enjoy helping with these kinds of systems problems, but there isn't much I can do if you come to me the night before the due date and say you can't install scikit. So please, if you want to procrastinate the rest of the assignment, by all means do, but do this part early.

2. Download the [code and data](downloads/pa5.tar.gz) for this assignment and unpack it. 

3. Look at the <code>all_data.txt</code>. This contains 13,529 tweets, collected by all of you. The tweets marked as irrelevant have been removed, and each tweet has been tagged with the majority label. For better or worse, this label will be treated as the gold standard that your classifier will try to learn. You will also see which student is responsible for each tweet, so if you see some particulary bad ones, you know who to take it up with...

4. A good first thing to do is to look at how the data is distributed. Here we have the following counts on our labels : 

   - 1648 negative

   - 4947 neutral

   - 6068 positive

   - 544 strongly negative

   - 322 strongly positive

    This is interesting. It means that our classifier can get 44% accuracy just by calling everything positive. Remember that since we will be using a Naive Bayes classifier, this liklihood of positive tweets will be encoded in the *prior*, and the classifier is trying to find the class to maximize the probability. I.e. :   
	
	$$argmax_{class} P(class | evidence) = prior \times liklihood = P(class)P(class | features)$$

	This means that the classifier will need stronger evidence to be convinced of the negativeness of a tweet than it will to be convinced of the positiveness of a tweet, meaning you will have to work harder to get it label tweets as negative. 

5. Let's try running it to see how well some really dumb classifiers do. I've seeded the code with a few features. 

	- baseline : this is a useless feature which has the same value for every example. I.e., the classifier will resort to guessing the most likely class (positive) all the time. 
	- ngrams : the words contained in the tweet (I am only using 1 grams. You should try changing this!). This is just a simple binary feature, indicating the presence or absence of a word. So for a the very useful tweet that would probably never be tweeted, 'I have the flu', our features would look something like [I=1, have=1, the=1, flu=1, cat=0, apple=0, walmart=0, upenn=0, lemonade=0...] etc, with 0 for all the words not in that tweet.

	Look at the code to see how it is set up. It is designed so you can pass features to the method <code>get&#95;x&#95;y</code> to specify with features to use. To run a baseline classifier, just run the code as is. 
<code>
	- $ python sentiment_classifier.py
</code>

	You will see something like 
<code>
	- Fold 0 : 0.44568
	- Fold 1 : 0.45144
	- Fold 2 : 0.44834
	- Train Average : 0.44853
	- Test Average : 0.44848
</code>
	This is the output of running a three fold cross validation. (Look at the slides if you don't remember what this means!!) 

	Note also that there are two accuracies reported. The train average is our accuracy if we run the classifer *on the data we trained on.* The test average is the accuracy when we run the classifier on *new data it has never seen before.* The test data is harder and reflects the real world case of how we'd want to use our classifier, so we only really care about test average.

6. We are unimpressed : this is exactly what we expected. The accuracy is 44%, meaning it guessed the positive label for everything. We can do better. Lets try adding in the words from the tweet, and see what happens. Go to line 240 and change 'baseline' to 'ngrams'. Rerun.

	Now we get
<code>
	- Fold 0 : 0.51264
	- Fold 1 : 0.52284
	- Fold 2 : 0.51863
	- Train Average : 0.82226
	- Test Average : 0.51803
</code>

	Look at that! We are feeling pretty damn good. Just the words alone without doing anything clever gives us a boost of 7 percentage points, and we can classify over half of the tweets correctly. 

7. Let's look at the features it learned. Open the file 'top_features.txt'. This will show you the top features ranked by log probability, i.e. $$log P(feature | class)$$ for each class. Here's what we see for the class 'strongly positive' : 

	- ('rt',) -6.42
	- ('kanye',) -6.78
	- ('iphone',) -6.85
	- ('coke',) -7.02
	- ('#missamerica',) -7.22
	- ('@missamerica',) -7.25
	- ('5s',) -7.32
	- ('love',) -7.52
	- ('nina',) -7.71
	- ('new',) -7.71

	Hmm. That's disappointing. 'love' and 'new' seem like okay features, but the rest? Is our classifier learning anything useful, or is it just memorizing which companies/people are mostly good and which ones are mostly bad, and classifying that way? If it is, that is definitely not what we want. We want a classifer that can differentiate between positive and negative tweets about the same company. 

8. Let's test if the classifier actually is learning useful things or just memorizing companies. We can test this by running a vairant of what is known as "leave one out cross validation." Instead of randomly dividing the data into train and test sets, we'll be smart about it. We will run one iteration for each student. In each iteration, we will train on the tweets from every student except one, and test on the held out student's tweets. Since each student chose a different company, this amounts to testing on a company that was not seen in training. Comment out line 241 and uncomment line 242 and rerun.  
<code>
	- Train Average : 0.82671 
	- Test Average : 0.38871 
</code>

	[Mother#*$&#^!](assets/img/football.gif) Memorizing companies in training is exactly what our classifier did. 

And so it goes with machine learning...so now your assignment : fix it. Make it work. Make the accuracy on the leave one out cross validation as high as humanly possible.  You will want to edit around lines 43 and 58 (you can and should define more functions as needed). There are some methods and code snippets for you to use for debugging and analysis purposes, if you want them. Take some time to go through the code and figure out what is happening before you start feature engineering. I am happy to answer any questions that come up. There are so many directions to take this, so get creative. This is the fun part! I'm not even being facetious this time. :-)

Good luck!! And may the best win!

