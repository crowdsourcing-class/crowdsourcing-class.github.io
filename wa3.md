---
layout: default
img: capitalist-greed
caption: Exploit the masses!
title: Homework 5 | Become a Requester
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 1st.</div>


Become a Requester<span class="text-muted">: Assignment 5</span> 
=============================================================

Last week, you built a classifier to predict whether or not an article was about gun violence. You were able to estimate how well your classifier did by using [cross validation](), and you probably ended up with some accuracies that were pretty damn near perfect. But a very good question to ask is, why train a model to label articles that already have labels?  The real point of machine learning is not to predict things that you already have answers to, but to try to predict new things. In this case, we want to see if our classifier can look at new articles that no one has labeled, and predict whether or not they are about guns. 

Predicting on data "in the wild" is much harder than predicting on the clean training data. Before, we cleaned your training data using the [Alchemy API]()'s state of the art processing, which gave us clean articles like this:

<i>"After a 14-year-old was gunned down Thursday night it appears Chicago went 42 hours without a shooting, but that streak came to an end Saturday afternoon when two people were shot near Ogden Park. Rarely is there a 42-hour period in Chicago without a shooting..."</i>

Now, your data has been scraped from the web, with cheaper, faster, hand-written-er (and drastically worse, why lie?) processing, so you might get articles like this:

<i>"Boy, 3, among 13 injured in Chicago park shooting .zone Boy, 3, among 13 injured in Chicago park shooting #adgSocialTools #adgSocialTools div.social_header #adgSocialTools div.social_main #adgSocialTools div.social_main img, #adgSocialTools div.social_footer img #adgSocialTools div.social_footer #adgSocialTools div.social_footer..."</i>

You can probably imagine that that 99% accuracy on cross validation may have been misleading. So this week we will get a real estimate of how well your classifier can do by taking the articles that your classifier thinks are gun-related, and asking workers on Crowdflower whether they agree or disagree with these predictions.


This assignment has two parts:

1. You will need to run your classifier from last week on 1.5 million unlabeled articles, and pull out the articles that it thinks are gun-related.
2. You will create a task on [Crowdflower]() in which workers will label a sample of the articles, and recalculate your classifier's accuracy.


###Part 1: Taking shots in the dark

For this part, you will use your classifier from last week to make predictions about never-before-seen data. You will need to make some changes to the code you wrote last week. There are some engineering details that you need to get right in order for everything to run smoothly, so read the instructions carefully and follow them closely.  

1. First, you need to download the [unlabeled data](). It is a healthy 1.4G, so maybe don't download it over the wifi you are broadcasting from your phone, or the crappy xfinity wifi connection that you are kind of picking up from the coffee shop next door. You can unpack the data using the following command. You should see two directories, one containing your training data (this is the same as last week) and one containing unlabelled data. The unlabelled data is in two parallel files: articles.txt contains the text of the articles that you will use for the classifier. urls.txt contains the urls from which this text came; you will use these in Part 2 of the assignment.

	<pre><code> $ tar -xzvf data.tgz
	$ ls data/*
	data/training-data:
	articles.txt
	
	data/unlabelled-data:
	articles.txt	urls.txt</code></pre>

2. You will the use the same classifier you built last week, but this time, instead of testing it with cross validation and priniting out the accuracy, you will train it on all your labeled data, and then use it to make predictions on your unlabelled data. To do this, download our [new code template](). This code should look very familiar to what you worked with last week, but has a few new functions added, which will handle the reading and vectorizing the unlabelled data. The only change you will need to make is to <b>replace the get_features() function with the get_features() function that you wrote</b> last week. If you used any auxilary functions as part of your get_features, you will need to copy those over too.  

	You can copy and paste your code, and if you are careful, it should run without complaining. To give you an idea of the main changes that needed to be made in order to have the classifier work on new data, read through the comments in the main method. Specifically, look at the function get_matricies_for_unlabelled(). The main difference is that when we convert our feature dictionary into a feature matrix, we need to make sure we use the same DictVectorizer object that we used to create the training data. This makes sense- we need to make sure that the column 627 in our new matrix means the same thing as column 627 in the training matrix, otherwise, the classifier will be totally helpless! You can also look at the function predict_unlabelled(). This should look very similar to the function you wrote to pull out misclassified examples in the homeword last week. 

3. Once you have copied over your feature function, you can run the program as follows. 

	<pre><code>$ python predict_unlabelled.py data/training-data/articles.txt data/unlabelled-data/articles.txt</code></pre>

	If you want to test your code to make sure it works, try running with a smaller file instead of using the whole data/unlabelled-data/articles.txt. When the code finishes, it will have created a file called classifier_predictions.txt, which contains the classifier predictions, one per line. E.g. the first line of classifier_predictions.txt is a '0' if the classifier thinks that the first article in data/unlabelled-data/articles.txt is not gun related. 

	You will almost definitely need to run this on biglab, unless you have a $!@#-ton of RAM. On biglab, it took XXX minutes to get predictions for all 1.5M articles. 

4. You now have three parallel files, each with 1,471,811 lines in it: data/unlabelled-data/articles.txt, data/unlabelled-data/urls.txt, and classifier_predictions.txt. For the next step, you will want to pull out just the urls of the articles which the classifier predicted as "gun-related"- that is, the lines for which classifier_predictions.txt has a '1'. You can use your favorite programming language to do this, or do it manually if you are bored and have nothing better to do. If you are interested, here is a great bash command to do it for you: 

	<pre><code>$ paste classifier_predictions.txt data/unlabelled-data/urls.txt | grep -e "^1" > positive_predicted_urls.txt</code></pre>

	This creates a new file, positive_predicted_urls.txt, with two columns, one with the label and one with the url. It uses three bash commands: paste just takes the contents of both files and pastes them side-by-side; grep searches for lines which match the pattern "^1", where the "^" just means "beginning of the line"; and the ">" symbol tells it to put the output into a new file, called positive_predicted_urls.txt.


###Part 2: ShootingsHIT

Whew, okay, enough python and bash for now! Its time to design a HIT on Crowdflower! The goal is to have the workers look at each of the URLs you gathered in step 4 of Part 1, and have them judge whether they agree that it is gun-violence-related. This should be a very painless process, hopefully. And look! There are even pictures!

1. Prep your data. You will need the list of urls to be in CSV format. The easiest way to do this will probably be to open the urls in a spreadsheet program like Google Docs or Excel. Then, you can use File->Export to CSV, and save the file. Make sure you add a header to the column, something informative like "url". 

2. Log onto [Crowdflower](). Click on "Your Jobs" -> "Create New Job." Then choose "Start from scratch."

	<img src="assets/img/crowdflower-screenshots/new-job.png" style="width: 500px;"/>

3. Choose the "spreadsheet" option for your data.

	<img src="assets/img/crowdflower-screenshots/upload-data.png" style="width: 500px;"/>

4. You will be abl to preview your data. It should look something like this.

	<img src="assets/img/crowdflower-screenshots/data.png" style="width: 500px;"/>

5. Next, design your interface. There is a nice WYSIWYG editor that will make it very easy to add questions. Just like on MTurk, you can flag variables using the {{VARIABLE_NAME}} syntax. When Crowdflower posts your HIT, it will replace your variable place holders with values from your CSV. E.g. everytime I write {{url}} in the HIT design, it will be replaced with an actual url from my data. Each row in my CSV corresponds to one HIT, so in each HIT, a different url will appear. Here is how my design looked, you are free to be more creative.
 
	<img src="assets/img/crowdflower-screenshots/UI-design.png" style="width: 500px;"/>

6. If you want to, you can also use the HTML editor. This makes it easy to add links to your URL. E.g.
	
	<img src="assets/img/crowdflower-screenshots/html.png" style="width: 500px;"/>

7. Once you are happy with your design, we will add in some test questions. These questions will be mixed into your data randomly, and used to evaluate how well the workers are doing. Crowdflower will walk through your data and ask you to label some of the articles yourself, and provide descriptions of why the answer is what it is. You should label about 50 articles to use as test questions.

 
	<img src="assets/img/crowdflower-screenshots/create-test.png" style="width: 500px;"/>
	<img src="assets/img/crowdflower-screenshots/label-test.png" style="width: 500px;"/>

8. That's basically it! Choose settings that reflect your feelings about the time and effort of your HIT, your morals, your politics, and your deep philosophies about the value of a hard days work. I had 3 workers judge each URL and paid a penny per URL. 

9. Now go! Post! And then obsessively watch the snazzy dashboard as your results come flooding in! 
	
	<img src="assets/img/crowdflower-screenshots/dashboard.png" style="width: 500px;"/>

	You can see what your HIT looks like by following the link at the bottom of your dashboard.
	
	<img src="assets/img/crowdflower-screenshots/view-hit.png" style="width: 500px;"/>

	Once the results are in, you can download them as a CSV file from the dashboard. We will do more work analyzing the results in the coming assignments.


The deliverables are: 
	- The final, labeled data you get from Crowdflower
	- A screenshot of your HIT 
	- A screenshot of your dashboard once the HIT has been completed 

Please turn in your files using turnin:
<pre><code>$ turnin -c nets213 -p crowdflower -v *</code></pre>

This assignment is due <b>Wednesday, October 1</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment.  
