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

Last week, you built a classifier to predict whether or not an article was about gun violence. You were able to estimate how well your classifier did by using [cross validation](http://en.wikipedia.org/wiki/Cross-validation_(statistics)), and you probably ended up with some accuracies that were pretty damn near perfect. But why train a model to label articles that already have labels?  The real point of machine learning is not to predict things that you already have answers to, but to try to predict new things. This week, we want to see if our classifier can look at new articles that no one has labeled, and predict whether or not they are about guns. 

Predicting on data "in the wild" is much harder than predicting on the training data. Before, we cleaned your training data using the [Alchemy API](http://www.alchemyapi.com/)'s state-of-the-art processing, which gave us clean articles like this:

<i>"After a 14-year-old was gunned down Thursday night it appears Chicago went 42 hours without a shooting, but that streak came to an end Saturday afternoon when two people were shot near Ogden Park. Rarely is there a 42-hour period in Chicago without a shooting..."</i>

Now, your data has been scraped from the web and cleaned with cheaper, faster, handwritten-er processing, so you might get articles like this beauty:

<i>"Boy, 3, among 13 injured in Chicago park shooting .zone Boy, 3, among 13 injured in Chicago park shooting #adgSocialTools #adgSocialTools div.social_header #adgSocialTools div.social_main #adgSocialTools div.social_main img, #adgSocialTools div.social_footer img #adgSocialTools div.social_footer #adgSocialTools div.social_footer..."</i>

You can probably imagine that that 99% accuracy on cross validation may have been misleading. So this week we will get a real estimate of how well your classifier can do by taking the articles that your classifier thinks are gun-related, and asking workers on Crowdflower whether they agree or disagree with these predictions.


This assignment has two parts:

1. You will need to run your classifier from last week on 1.5 million unlabeled articles, and pull out the articles that it thinks are gun-related.
2. You will create a task on [Crowdflower](http://www.crowdflower.com/) to have workers assess your predictions. You will use this to recalculate your classifier's accuracy.


###Part 1: Taking shots in the dark

For this part, you will use your classifier from last week to make predictions about never-before-seen data. You will need to make some changes to the code you wrote last week. There are some engineering details that you need to get right in order for everything to run smoothly, so read the instructions carefully and follow them closely. 

1. First, ssh into your account on biglab. You will almost definitely crash your laptop if you try to work locally, unless you have a $!@#-ton of RAM, so now is as good a time as any to learn how to read, write, and run code from the command line! Bonus, we already have the data on biglab for you, so you don't need to download it. It is in the directory <code>/blah/blah/blah</code>. You can look at the files in a directory by typing <code>ls</code> (for "list"). E.g.

	<pre><code>$ ssh epavlick@biglab.seas.upenn.edu
	epavlick@biglab.seas.upenn.edu's password: 
	SEAS SuSE Linux 13.1
	epavlick@big05:~> ls blah/blah/blah
	data/training-data:
	articles.txt
	
	data/unlabelled-data:
	articles.txt	urls.txt</code></pre>

	You should see two directories, one containing your training data (this is the same as last week) and one containing unlabelled data. The unlabelled data is in two parallel files: <code>articles.txt</code> contains the text of the articles that you will use for the classifier. <code>urls.txt</code> contains the urls from which this text came; you will use these in Part 2 of the assignment.

2. You will the use the same classifier you built last week, but this time, instead of testing it with cross validation and priniting out the accuracy, you will train it on all your labeled data, and then use it to make predictions on your unlabelled data. To do this, download our [new code template](http://www.seas.upenn.edu/~epavlick/nets213/predict_unlabelled.py) (the easiest way would be to use [wget](https://www.gnu.org/software/wget/manual/html_node/Simple-Usage.html#Simple-Usage)!). This code should look very familiar to what you worked with last week, but has a few new functions added, which will handle the reading and vectorizing of the unlabelled data. The only change you will need to make is to <b>replace the <code>get_features()</code> function with the <code>get_features()</code> function that you wrote</b> last week. If you used any auxilary functions as part of your <code>get_features</code>, you will need to copy those over too.  

	You can copy over your function, and if you are careful, it should run without complaining. (Note: To give you an idea of the main changes that needed to be made in order to have the classifier work on new data, read through the comments in the main method. Specifically, look at the function <code>get_matricies_for_unlabelled()</code>. The main difference is that when we convert our feature dictionary into a feature matrix, we need to make sure we use the same <code>DictVectorizer</code> object that we used to create the training data. This makes sense- we need to make sure that the column 627 in our new matrix means the same thing as column 627 in the training matrix, otherwise, the classifier will be totally helpless! You can also look at the function <code>predict_unlabelled()</code>. This should look very similar to the function you wrote to pull out misclassified examples in the homeword last week.)

3. Once you have copied over your feature function, you can run the program as follows. 

	<pre><code>$ python predict_unlabelled.py data/training-data/articles.txt data/unlabelled-data/articles.txt</code></pre>

	You might want to test your code to make sure it works before running on the full 1.5M articles, so try running with just a few lines of data/unlabelled-data/articles.txt. You can do this by giving the code a third argument, e.g. to predict for the first 10 articles, run

	<pre><code>$ python predict_unlabelled.py data/training-data/articles.txt data/unlabelled-data/articles.txt 10</code></pre>

	This will still take a few minutes, since you still need to train on all 70K training articles! 

	If it works, run on the full 1.5M articles. Once you start it, don't hold your breadth. Maybe go grab coffee...or a nice dinner downtown...go for a leisurly hike. It took me about 20 minutes to finish on biglab. When the code finishes, it will have created a file called <code>classifier_predictions.txt</code>, which contains the classifier predictions, one per line. E.g. the first line of <code>classifier_predictions.txt</code> is a '0' if the classifier thinks that the first article in data/unlabelled-data/articles.txt is not gun related. My classifier found a little under 190,000 articles that it thought were gun-related. You can check this with the bash command we mentioned in class: 
	<pre><code>cat classifier_predictions.txt | sort | uniq -c </code></pre>.

4. You now have three parallel files, each with 1,471,811 lines in it: <code>unlabelled-data/articles.txt</code>, <code>data/unlabelled-data/urls.txt</code>, and <code>classifier_predictions.txt</code>. For the next step, you will want to pull out just the urls of the articles which the classifier predicted as "gun-related"- that is, the lines for which classifier_predictions.txt has a '1'. You can use your favorite programming language to do this, or do it manually if you are bored and have nothing better to do. If you are interested, here is a great bash command to do it for you: 

	<pre><code>$ paste classifier_predictions.txt data/unlabelled-data/urls.txt | grep -e "^1" > positive_predicted_urls.txt</code></pre>

	You should also pull out the negative predictions, and put them in a separate file:

	<pre><code>$ paste classifier_predictions.txt data/unlabelled-data/urls.txt | grep -e "^0" > negative_predicted_urls.txt</code></pre>

	This creates a new file, positive_predicted_urls.txt, with two columns, one with the label (which will always be '1'), and one with the url. It uses three bash commands: <code>paste</code> just takes the contents of both files and pastes them side-by-side; <code>grep</code> searches for lines which match the pattern <code>^1</code>, where the <code>^</code> just means "beginning of the line"; and the "<code>></code>" symbol (often read as "redirect") tells it to put the output into a new file, called <code>positive_predicted_urls.txt</code>.

5. Finally, you will need to get a sample of these articles to label on Crowdflower. We will label 500 positive predictions, and throw in a few negative predictions (which we will use for quality control. Again, some bash to the rescue:

	<pre><code> $ cat positive_predicted_urls.txt | shuf | head -500 > sample.txt
	$ cat negative_predicted_urls.txt | shuf | head -50 >> sample.txt</code></pre>
	
	This creates a new file, <code>sample.txt</code> which contains a random 500 lines from <code>positive_predicted_urls.txt</code> and a random 50 lines from <code>negattive_predicted_urls.txt</code>. Again, it uses three bash commands: <code>cat</code> (for "concatenate") just dumps the entire contents of a file; <code>shuf</code> scrambles the order of the lines; <code>head -n</code> takes the top <code>n</code> lines of its input and ignores the rest. We use <code>>></code> in the second line in order to append to a file that already exists. If we used <code>></code>, we would overwrite the lines that we just put there in the first command!

	For good measure, you might want to shuffle <code>sample.txt</code>, so that the negative examples are all at the bottom. Try to figure out how to do it in bash! 

###Part 2: ShootingsHIT

Whew, okay, enough python and bash for now! Its time to design a HIT on Crowdflower! The goal is to have the workers look at each of the URLs you gathered in step 4 of Part 1, and have them judge whether they agree that it is gun-violence-related. This should be a very painless process, hopefully. And look! There are even pictures!

1. Prep your data. You will need the list of urls to be in CSV format. The easiest way to do this will probably be to open <code>sample.txt</code>, or whatever you called your file, in a spreadsheet program like Google Docs. Then, you can use File->Dowload as->CSV, and save the file. Make sure you add a header to the columns, something informative like "url" or "stuff." 

2. Log onto [Crowdflower](). Click on "Your Jobs" -> "Create New Job." Then choose "Start from scratch."

	<img src="assets/img/crowdflower-screenshots/new-job.png" style="width: 500px;"/>

3. Choose the "spreadsheet" option for your data.

	<img src="assets/img/crowdflower-screenshots/upload-data.png" style="width: 500px;"/>

4. You will be able to preview your data. It should look something like this.

	<img src="assets/img/crowdflower-screenshots/data.png" style="width: 500px;"/>

5. Next, design your interface. There is a nice WYSIWYG editor that will make it very easy to add questions. Just like on MTurk, you can flag variables using the \{\{VARIABLE_NAME\}\} syntax. When Crowdflower posts your HIT, it will replace your variable place holders with values from your CSV. E.g. everytime I write \{\{url\}\} in the HIT design, it will be replaced with an actual url from my data. Each row in my CSV corresponds to one HIT, so in each HIT, a different url will appear. Here is how my design looked, you are free to be more creative.
 
	<img src="assets/img/crowdflower-screenshots/UI-design.png" style="width: 500px;"/>

6. If you want to, you can also use the HTML editor. This makes it easy to add links to your URL. E.g.
	
	<img src="assets/img/crowdflower-screenshots/html.png" style="width: 500px;"/>

7. Once you are happy with your design, you will need to add in some test questions. These questions will be mixed into your data randomly, and used to evaluate how well the workers are doing. Crowdflower will walk through your data and ask you to label some of the articles yourself, and provide descriptions of why the answer is what it is. You should label about 50 articles to use as test questions.

	<img src="assets/img/crowdflower-screenshots/create-test.png" style="width: 500px;"/>
	<img src="assets/img/crowdflower-screenshots/label-test.png" style="width: 500px;"/>

8. That's basically it! Choose settings that reflect your feelings about the time and effort of your HIT, your morals, your politics, and your deep philosophies about the value of a hard days work. I had 3 workers judge each URL and paid a penny per URL. 

9. Now go! Post! And then obsessively watch the snazzy dashboard as your results come flooding in! 
	
	<img src="assets/img/crowdflower-screenshots/dashboard.png" style="width: 500px;"/>

	You can see what your HIT looks like by following the link at the bottom of your dashboard.
	
	<img src="assets/img/crowdflower-screenshots/view-hit.png" style="width: 500px;"/>

	Once the results are in, you can download them as a CSV file from the dashboard. Answer the few quick questions [here]() about your results. We will do more work analyzing the results (specifically, the worker's quality) in the coming assignments.


The deliverables are: 
	1. The final, labeled data you get from Crowdflower, as a csv file.
	2. A screenshot of your HIT, as it looked to the workers.
	3. A screenshot of your dashboard once the HIT has been completed.
	4. Your responses in the questionnaire. 

Like before, please turn in your files using turnin:
<pre><code>$ turnin -c nets213 -p crowdflower -v *</code></pre>

This assignment is due <b>Wednesday, October 1</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment.  
