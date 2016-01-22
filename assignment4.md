---
layout: default
img: ML
caption: Crowdsourcing FTW!
title: Homework 4 | Playing with Classifire
active_tab: homework
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->

<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 24.</div>

Training a classifier<span class="text-muted"> : Assignment 4</span> 
=============================================================
In the remaining weekly homework assignments, the class will be working to build a large database of gun violence incidents across the country. As computer scientists, we often take for granted the large amounts of data that are available. Other fields, however, such as the social sciences, are often limited in their ability to carry out robust studies because of a lack of data. There is a lot of room for smart, creative people like yourselves to make big strides in computational approaches to social science disciplines like economics, sociology, political science, and public health. And even if it is just [dressed-up statistics](http://en.wikipedia.org/wiki/Data_science#Criticism), getting to use sexy names like "data science" and "machine learning" will make your mother proud.

We will be collecting data for our database from articles which are published in local newspapers across the country. We will use crowdsourcing to extract the structured information from these articles, but as a first step, we need to collect articles that describe incidences of gun violence. This is easier said than done. We can easily grab a handful of articles manually, but in order to build a meaningful database, we want to be able to gather data from a lot of articles, too many to do by hand. This is a picture perfect use of machine learning. If we can find a small number of examples of gun-related articles and of non-gun-related articles, we can train a model to predict for a million or more articles, with hopefully reasonable accuracy, which articles describe gun violence and which do not. 

We have already collected training data for you. Chris crawled a [NY Times blog about gun violence](http://nocera.blogs.nytimes.com/category/gun-report/) and gathered about 9,000 articles describing gun-related crimes. We are pulling examples of non-gun-related articles from a [local news corpus](ihttp://www.cs.jhu.edu/~anni/papers/alnc_lrec14.pdf) from Johns Hopkins.  In total you will have about 70K articles (~7 non-gun articles for every 1 gun article) to train your classifier. 

##To Do

Your task will be to build a classifier following our guidelines, and [respond to some questions about the process](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). After that, you are free to experiment. We have held out some secret data that we will use to test your classifiers. The student/s with the best performing classifier will be given $1,000,000! Or extra credit. Probably extra credit.

1. [Download the data](assignments/downloads/articles.gz) and unzip it with the Unix <code>gunzip</code> command. The data is in the format of one article per line. Each line has two values (tab separated): a label (0 for non-gun, 1 for gun), and the text of the article. 

2. [Download the code template](assignments/downloads/classifier_template.py) and look through the function stumps. These steps should seem familiar if you think back to Wednesday's lecture. Look especially closely at the functions flagged with "TODO." These are the ones you will edit.

	<h3>Rule Based Classifiers</h3>

3. The simplest way to build a classification algorithm is to use a rule based system. Look at the function rule_based_classifier(). This function doesn't bother itself with mathy mumbo jumbo, it just looks for keywords it thinks are indicative of gun-related articles. If one of the keywords appears, it predicts "1" (or "gun-related") and otherwise it picks "0". Right now we use just one keyword, "shooting." Try running the code with this command and see how well this very simple method works.

	Now experiment with adding a few more keywords. See how high you can make the accuracy using this method. Experiment with combinations of keywords as well. Feel free to get creative with your conditional statements! You will answer a few questions about this in the questionnaire. 

	<pre><code> python classifier_template.py articles.txt </code></pre>

	<h3>Crash Course in Machine Learning</h3>

4. To understand and complete the next part of the assignment, you’re going to first go through a quick crash course in Machine Learning. This isn't intended to give you a deep insight behind the dressed up statistics but instead will introduce you to the fundamental concepts and some ML vocabulary necessary for this assignment. 

	So what is Machine Learning? 

	<i>Definition by Tom Mitchell (1998): </i>

	Machine Learning is the study of algorithms that
	<ul> 
	<li>Improve their performance P </li> 
	<li>At some task T </li>
	<li>With experience E. </li>
	</ul>
	A well-defined learning task is given by <b><P,T,E></b>.

	More simply, Machine Learning is the field of computer science where algorithms are not explicitly programmed and adapt by analyzing data. A very simple case of Machine Learning is Linear Regression where the parameters of the line are adjusted to fit the data.  Machine Learning algorithms are broadly classified into two kinds – Supervised Learning and Unsupervised Learning algorithms. Supervised Learning algorithms can be further classified into Regression Algorithms and Classifiers. For this assignment we will only concern ourselves with Supervised Learning Algorithms, specifically Classifiers. 

	A Classifier, much as the name suggests, takes in data about a certain entity and then makes a prediction as to which class that entity belongs to. For example, our classifier will take data in the form of whether certain words show up in an article and then predict if the article is a Gun violence related article or not. 

	For any Supervised Machine Learning algorithm to learn, it requires labeled training data. The data usually looks something like this: 

	<img src="assets/img/matrix.png" style="width: 300px;"/>

	The data is structured as an <b><i>N x (M+1)</i></b> Matrix. Each row of the matrix corresponds to one entity (an individual data point). Thus we say this dataset has <b><i>N</i></b> instances. Each column corresponds to a "Feature". A feature is nothing but a particular attribute or quality about our entity. For example, the existence of the word "Gun" in an article is a feature. We can model this feature as a Boolean, where 0 corresponds to the word "Gun" missing from the article and 1 means that it exists. The matrix has <b><i>M+1</i></b> columns. The first <b><i>M</i></b> columns correspond to the <b><i>M</i></b> features observed about our data entities. The last column is our label for our data – i.e. the class that instance belongs to. In our Gun Article database, <b><i>N</i></b> corresponds to the 57,333 entries. The existence of a particular word (e.g. "Gun") in an article is a feature and 0 or 1 is the label corresponding to whether the article is about gun violence or not. So <b>x<sub>i</sub><sup>j</sup> </b>corresponds to the value of the <b>j<sup>th</sup></b> feature of the <b>i<sup>th</sup></b> instance. And <b>y<sub>i</sub></b> is the label of the <b>i<sup>th</sup></b> instance. 

	So once we have data that is structured in this fashion, a ML classifier takes each of the instances and constructs a model, making associations between the feature values and the labels. Once this model is generated, the algorithm can take in instances without any labels and use the model to predict what label that instance might have. And viola! You are now Machine Learning literate!


	<h3>Decision Trees</h3>
5. A more algorithmic approach to creating a rule-based classifier can be done using Decision Trees. Decision Trees are a class of Machine Learning algorithms that use a tree-like structure to model certain decisions and map them to their corresponding outcomes. The image below is a very simple example of a decision tree classifier.

	<img src="assets/img/decision-tree.gif" style="width: 500px;"/>

	A Decision Tree takes an unmapped feature from the list of features and creates a node. From that node, each branch corresponds to one of the possible values of that feature (i.e. the feature Outlook has the possible values Sunny, Overcast and Rain). The tree is recursively built using this process till the corresponding classification at each of the leaf nodes is perfect / we run out of features / the maximum height has been reached. There are different Decision Tree algorithms and they all fundamentally differ in the mathematics of which features they pick at each step. If you are interested in learning more about Decision Trees, read [this chapter](http://www.cs.princeton.edu/courses/archive/spr07/cos424/papers/mitchell-dectrees.pdf) and look into the courses [CIS 419/519](http://www.cis.upenn.edu/~cis519/fall2015/) and [CIS 520](https://alliance.seas.upenn.edu/~cis520/wiki/).

	While we won’t obsess over the math that goes into how Decision Trees work, it’s useful to know that they’re surprising good at classification tasks (much like this one!). The rule based classifier you created using conditional statements in the function <code> rule_based_classifier()</code> was essentially a Decision Tree. Draw the Rule Based Decision Tree you came up with in part 3 using your favourite diagram-making tool. (I like [draw.io](https://www.draw.io/))


6. Let's now create an actual decision tree. Uncomment the 3 lines in the Decision Tree section and run the script. You will need the [Graphviz](http://www.graphviz.org/) library installed for this to work. The code takes a couple seconds to run. The Decision Tree diagram generated is shown below.

	<img src="assets/img/decision-tree.png" style="width: 350px;"/>

	This dummy tree classifies every article based on only the word "gun". Each box contains a couple values. For the root box, "gun <= 0.5" refers to the feature "gun" and the two branches - one each corresponding to the value of "gun" being less than 0.5 and more than 0.5. Because our data is binary, this is exactly the same as "gun" being 0 or 1. Gini corresponds to the [Gini Coefficient](https://en.wikipedia.org/wiki/Gini_coefficient) which is a statistical measure of uniformity. A lower Gini index corresponds to a more uniform dataset. "Samples" corresponds to the total number of instances falling under this classification of the tree. As we're looking at the root node, "Samples" equals the entire dataset of 57,333 entities. Value shows the classification split i.e. at the root node we have 50,129 non Gun Violence related articles and 7204 Gun violence related articles. Class is the dominant classification at this stage. It's also the label the Decision Tree would assign to our instance if the decision process terminated at the given node. This detail is unimportant for internal nodes but crucial for leaf nodes, which assign the final classification.


	Now look at <code>get_dtree_features()</code> and add the features you used in your Rule Based Classifier from part 2. Re-run the script and look at the generated Decision Tree. Compare it to the Decision Tree you drew. What are the similarities and differences? Did your accuracy improve? You will later note these observations in the questionnaire.

	<div class="panel panel-danger">
	<div class="panel-heading" markdown="1">
	<i>Extra Credit</i>
	</div>
	<div class="panel-body">

		Take your optimized Decision Tree and reverse engineer it to create a Rule Based Classifier. Complete the function <code>extra_credit_classifier()</code> to do this. How does the accuracy of this classifier relate with that of your optimized Decision Tree? 

	</div>
	</div>

7. Decision Trees are a very powerful classification tool but are prone to over fitting. Play around with the code and add more keywords. You'll find your accuracy begins to decline after a certain point. One easy way to avoid this is limiting the height of the tree. This can be done using the <code>max_depth</code> attribute. Replace the <code>None</code> with an integer value (try a couple different values). 

	<pre><code>  clf = DecisionTreeClassifier(max_depth=None)</code></pre>

	Change both the keywords and the tree height and see how accurate you can make your classifier. You will submit the tree diagram output of your most accurate Decision Tree.

	<h3>Statistical Models</h3>
8. You can get surprisingly far using just a few keywords. But why stop there? Why not use ALL THE KEYWORDS!? That is precisely what statistical models are for! 

	For the statistical model, your code will really just need to do one thing. That is, you need to build two side-by-side data structures: a *feature matrix* and a *label vector*. Your feature matrix will represent one article on each row, and each column will correspond to some "feature" you can observe about that article. The label vector will give the correct labels of each article, so that the nth element of the vector is 1 if the nth row of the matrix corresponse to a gun-related article.
	
	Look at the function get_features(). The template builds a stupid classifier whose feature matrix contains only one feature, which has the same value for every article. Try running it as follows and see that you get the below output. Here, the classifier is trying to make predictions, but has absolutely no information to work with. As a result, it just guesses based on the [prior probability](http://en.wikipedia.org/wiki/Prior_probability). I.e. this accuracy is the result of the classifier chosing the label "0" (or "non-gun-related") for every article.

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

	Try it and then record your experience in the [questionnarie](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form). For your classifier analysis, you need to look at feature weights that have been learned, and will need to see the predictions the classifier makes for individual articles. Look at the [functions available to you](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) through the LogisiticRegression classifier to get you started. 

And with that- Good luck! Start early and have fun! If robots are going to run the world, they need to first know the difference between articles about gun violence and articles about the weather. So go! Make it happen! 

Don't forget to answer all of the questions in the [questionnaire](https://docs.google.com/forms/d/1whhkFQ0ndN9E_XOsuqoxpRIAJcnUZqKKx1eAioyU9wg/viewform?usp=send_form) when you are done, and to submit your final classifier code, a picture of the tree you drew and the generated diagram of your optimal Decision Tree via turnin. 

<pre><code>$ turnin -c nets213 -p classifier -v classifier.py rule-based-tree.png decision-tree.png</code></pre>

Your code and questions are due <b>Wednesday, September 24</b>. You can work in pairs on this assignment.  You must declare the fact that you are working together when you turn in the questionnaire.  If you are working with a partner, only one of you needs to turn in the code, but you must specify who will be turning it in on the questionnaire. You cannot add or change partners after the code and questionnaire are submitted.

<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 5 points of your overall grade in the course.  The rubric for the assignment is given below.

* 1 points - Rule Based Classifier.
* 1 points - Decision Tree Drawing.
* 1 points - Optimizing your Decision Tree and the Decision Tree diagram.
* 1 points - Statistical Unigram Model.
* 1 points - Survey Questions.
* Extra credit (1 point) - Reverse engineering the optimal Decision Tree as a rule based classifier.

</div>
</div>

Related Projects
================


* [Gun Violence Archive](http://gunviolencearchive.org)
* [Mass Shooting Tracker](http://shootingtracker.com/wiki/Main_Page)
* [Uniform Crime Reporting Statistics](http://www.ucrdatatool.gov/Search/Crime/State/StatebyState.cfm)
* [Police-shooting Database](http://regressing.deadspin.com/deadspin-police-shooting-database-update-were-still-go-1627414202) 
- [Gawker article](http://gawker.com/what-ive-learned-from-two-years-collecting-data-on-poli-1625472836), [NPR story](http://www.npr.org/2014/08/21/342228794/ferguson-turns-lens-on-police-involved-killings-but-some-facts-are-few)
* [Fatal Encounters](http://www.fatalencounters.org)
* [Rates of gun homicides by country compiled by The Guardian](http://www.theguardian.com/news/datablog/2012/jul/22/gun-homicides-ownership-world-list)
* [USA TODAY research reveals flaws in mass-killing data](http://www.usatoday.com/story/news/nation/2013/12/03/fbi-mass-killing-data-inaccurate/3666953/)



