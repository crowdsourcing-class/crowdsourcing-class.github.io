---
layout: default
img: capitalist-greed
caption: Exploit the masses!
title: Homework 6 | Building the database 
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 22nd.</div>


Building a database<span class="text-muted"> : Assignment 6</span> 
=============================================================

Okay, so we've been talking all semester about this gun violence database. And we've been making all sorts of big promises to Doug and the other epidemiologists. But, what have we gotten so far: "Here are some articles that we are about 10% confident are about guns, and also, the word "shooting" is a good feature." Nothing to write home about. So time to deliver. Let's take these articles and turn it into something useful. 

We will do this using (surprise!) crowdsourcing. This week, you are going to ask Crowdflower workers to read through the articles that you all identified as gun related back in homework 5, and pull out the key facts in a principled way. Your primary goal is to design an interface that helps them do this quickly and accurately. We will walk you through some initial steps to get you started on the design, but you are welcome to go in your own direction.  

Your deliverables will be:
1. Two csv files from Crowdflower containing the information the workers extract
2. Screen shots of your two HIT designs
3. Reponses about your findings in [this questionnaire]().

You will might want to work in teams for this porject. These HITs will require more time for the crowd workers, and so should pay a bit more than the previous ones. Don't be a jerk and pay them pennies just cause your account is low! Buddie up with someone, or feel free to add some funds to your account. (We didn't have a text book for this class, remember? So we've been easy on your budget so far.)

###Code, data, and signing up for more emails

1. In assignment 5, you guys had workers label your classifier's results. To give you data to work with, we've pulled together 200 of the urls your workers called "gun related." We've also written some code to do some text processing for you, which we will talk about in a few steps. You can download all the code and data [here](). 

	<pre><code>$ wget assignment6.tgz
	$ tar -xvzf assignment6.tgz
	$ ls assignment6/
	clean_and_process_data.py	convert_to_csv.py		gun-violence-urls.txt
	</code></pre>

2. You should see three files. <code>gun-violence-urls.txt</code> contains 198 urls that your workers labeled as gun-related in the previous assignment. <code>clean_and_process_data.py</code> is a script which will perform basic text processing to clean up your articles and help pull out some potentially useful information (like names and locations). <code>convert_to_csv.py</code> will put your data into a csv that can be uploaded to Crowdflower. 

3. In order to do the text processing, we will be using the [Alchemy API](http://www.alchemyapi.com/api/calling-the-api/). This is a super awesome professional API which does a lot of very complicated NLP for you and makes it seem easy. In order to use it, you will need to [sign up for an account](http://www.alchemyapi.com/api/register.html) and get an API key. The default account will give you 1,000 API calls a day. This is probably enough for this assignment- you will need two calls per url, so if you only mess up one and a half times, you should still be within your daily limit. However, if you want to explor it more (which you really should! its awesome!) you can sign up for an academic account, which will give you 30,000 calls a day. If you want to do this, let me know. It just requires sending an email to the sales team, and you can copy the email I used to request my academic license.

###HIT Design

This assignment is due <b>Wednesday, October 22</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment.  
