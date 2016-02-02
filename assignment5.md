---
layout: default
img: capitalist-greed
caption: Exploit the masses!
title: Homework 5 | Become a Requester
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
  This assignment is due before class on Wednesday, October 1st.</div>


Become a Requester<span class="text-muted"> : Assignment 5</span> 
=============================================================

Last week, you built a classifier to predict whether or not an article was about gun violence. You were able to estimate how well your classifier did by using [cross validation](http://en.wikipedia.org/wiki/Cross-validation_(statistics)), and you probably ended up with some accuracies that were pretty damn near perfect. But why train a model to label articles that already have labels?  The real point of machine learning is not to predict things that you already have answers to, but to try to predict new things. This week, we want to see if our classifier can look at new articles that no one has labeled, and predict whether or not they are about guns. 

Predicting on data "in the wild" is much harder than predicting on the training data. There are a million reasons for this. To name a few:

* Your training data contained 10% gun-related articles. If you download all the articles posted on a given day, it is probably not the case (let's hope to God!) that 10% of them describe gun violence. So you are now looking for a tiny needle in a huge haystack, whereas your classifier is expecting something very [different](assets/img/needle-in-a-haystack.png).  
* Your training data was nicely cleaned and contained sentences like: <i>"After a 14-year-old was gunned down Thursday night it appears Chicago went 42 hours without a shooting."</i> Scraping articles from the web can yield senences like this beauty: <i>"Boy, 3, among 13 injured in Chicago park shooting .zone Boy, 3, among 13 injured in Chicago park shooting #adgSocialTools #adgSocialTools div.social_header #adgSocialTools div.social_main #adgSocialTools div.social_main img, #adgSocialTools div.social_footer img #adgSocialTools div.social_footer #adgSocialTools div.social_footer..."</i>

You can probably imagine that that 99% accuracy on cross validation may have been misleading. So this week we will get a real estimate of how well your classifier can do by taking the articles that your classifier thinks are gun-related, and asking workers on Crowdflower whether they agree or disagree with these predictions.

This assignment has three parts:

1. You will need to build a crawler to collect news articles from the web. Some of these will hopefully be about gun violence, but many will not. 
2. You will need to run your classifier from last week on your crawled articles, and pull out the articles that the classifier thinks are related to guns.
3. You will create a task on [Crowdflower](http://www.crowdflower.com/) to have workers assess your predictions. You will use their labels to recalculate your classifier's accuracy.

**Extra Credit**: We will run a little competition on the assignment for extra credit. The task is simple: whoever can deliver the largest list of urls to acutal, gun-violence articles will get extra credit, and much loving praise. This can mean you build a super-accurate classifier, or a super effective crawler, or both. We will describe the details of the competition at the end of the assignment. 

<h3>Part 1: Pub(lication) Crawl</h3>

Part 1 of your assignment is to build a web crawler! This is up there as one of the most important life skills you will ever learn, alongside balancing a budget and feeding yourself. And like most essential life skills, you don't need to be great at building a web crawler, you just need to know enough to get by. This section of the assignment will introduce two tools for collecting urls from the web, and walk you through running the templates we provide. Then, we will ask you to extend and improve what we show you in order to collect as many gun-violence article urls as you can.

1. **Download the code** First things first: download the [code templates](http://crowdsourcing-class.org/assignments/downloads/assignment5.tgz) for this assignment. When you unpack the archive, you should see the following directories. 
	
	<pre><code> $ wget http://crowdsourcing-class.org/assignments/downloads/assignment5.tgz
	$ tar -xzvf asssignment5.tgz 
	$ ls assignment5	
	part_1_crawling part_2_classification</code></pre>

2. **Read through python_crawler.py** We will first deal with the code in part_1_crawling. You should see that this directory contains three files, like below. Open the file called python_crawler.py and read through the code and comments. You don't need to understand every line (TBH, I copy and paste code from the internet all the time without understanding it) but you should have an idea of what is happening, since you will need to modify it later. 

	<pre><code> $ ls assignment5/part_1_crawler/
	bing_api.py  get_clean_text.py  python_crawler.py </code></pre>

3. **Use Python to crawl Gun Report blog** At a high level, the code in python_crawler.py is a basic web crawler. It will begin on a webpage that we specify, and it will look for all of the hyperlinks on that page. Everytime it finds a link, it will print the link, and then follow it. When if follows a link, it will start doing the exact same thing-- looking for more links, printing them, and then following them. For people who have taken algorithms, you will recognize this as a standard [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search). For those of you who haven't, you will recognize this as a perfectly common sense way to look for links, regardless of fancy names. The code written now scrapes links from the [Gun Report Blog](http://nocera.blogs.nytimes.com/category/gun-report/). This is the same site Chris used to collect training data for your assignment last week. Trying running the code, and see what output you get. The below commands will run the crawler and print the links to a file called gun_report_urls.txt. The second two lines will remove duplicated urls in your list. Note this crawler is not very fast. For me, running the code took about 10 minutes and produced 8,884 unique urls.

	<pre><code> $ python python_crawler.py > gun_report_urls.txt
	$ cat gun_report_urls.txt | sort | uniq > tmp #remove duplicate urls and put all the unique ones in tmp
	$ mv tmp gun_report_urls.txt # replace the old list of urls with the new list of only unique urls
	$ wc -l gun_report_urls.txt # print the number of lines in the file.
	8884 </code></pre>

4. **Modify python_crawler.py** You should now modify the code in python_crawler.py in order to crawl the [Gun Violence Archive](http://www.gunviolencearchive.org/) website. You should save the urls you collect to a file called gun_archive_urls.txt, and submit this file when you turnin your assignment.

5. **Sign up to access the Bing API** Crawling websites like we did above is a common way to collect data from the web. Another very common way is through the use of APIs. Here, we will show you how to use the Bing search API. In short, and API allows your program to issue web queries in much the same way you do when you use a browser. To use the Bing API, you will need to register with Microsoft [here](https://datamarket.azure.com/dataset/bing/search) (sign up for the free account). Once you are registered, go to **My Account** > **My Data** and click on the **Use** link next to **Bing Search API**. You can play with issuing different search queries in the browser here if you want. But, mainly, you will need to **Show Primary Account Key** and copy and paste your key into the bing_api.py script where it says YOUR KEY HERE.

6. **Use the Bing API to collect urls** Like before, read through the code in bing_api.py and try to understand what is happening. Again, you will need to modify it, so familiarize yourself with the url request structure, and the parameters that you are passing. You can run the code similarly to before, as follows:

	<pre><code> $ python bing_api.py > bing_urls.txt
	$ cat bing_urls.txt | sort | uniq > tmp #remove duplicate urls and put all the unique ones in tmp
	$ mv tmp bing_urls.txt # replace the old list of urls with the new list of only unique urls
	$ wc -l bing_urls.txt # print the number of lines in the file.
	140 </code></pre>

7. **Modify bing_api.py** Now, edit the bing_api.py file in two ways. First, try at least three different queries, and output the results of each one. Second, change the printing to print not just the url, but also the title and date associated with the article. Your script should print the three fields (url/date/title) separated by tabs. You should print the output to a file called bing_api_results.txt, and submit this file when you turn in your assignment.

8. **Go forth and do** At this point, you have a lot of tools at your disposal to collect urls and articles. You should try to collect as many as possible. At a minimum, you are **required** to submit the urls you collect from the Gun Violence Archive in Step 4, and the Bing API urls you collect using the three queries in Step 7. We will give extra credit for students who collect the most actual gun violence urls. Below are some ideas you might want to consider for increasing the number of urls you collect:

	* Crawl entire news sites (e.g. New York Times) and grab all articles (not just gun-related ones). Then rely on your classifier to filter the list for you. You can get a list of local news sites [here](http://newspapermap.com/).
	* Adapt your python crawler to scrape other gun violence awareness sites like [Fatal Encounters](http://www.fatalencounters.org/) or [the Guardian's gun violence site](http://www.theguardian.com/news/datablog/2012/jul/22/gun-homicides-ownership-world-list) 
	* Change the date ranges you search using Bing in order to dig up older articles
	* Try fancier crawling tools like [scrapy](http://scrapy.org/) or [Selenium](http://selenium-python.readthedocs.org/)

9. **Download and install beautiful soup** At this point, you have done a lot of strenuous work to collect an awesome list of urls of articles. But, ultimately, you don't just want the urls, you want the articles themselves. So now, we will use a package called [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). Although better tools exist, BeautifulSoup is probably the most popular python package for parsing html, so it is a useful tool to know. You can install it as follows:

	<pre><code> $ sudo pip install bs4</code></pre>

10. **Extract the article text from your urls** We have provided a script that will extract the text for you, and output a file with one article per line in the format "url \t article_text". In order to run it, you should gather up all the urls you have collected and put them in a file with one url per line. Then run the command below. In Part 2, you will use the output of get_clean_text.py as input to your classifier.

	<pre><code> cat list_of_urls.txt | python get_clean_text.py > articles_and_urls.txt </code></pre>


###Part 2: Taking shots in the dark

For this part, you will use your classifier from last week to make predictions about never-before-seen data. You will need to make some changes to the code you wrote last week. There are some engineering details that you need to get right in order for everything to run smoothly, so read the instructions carefully and follow them closely. 

1. First, ssh into your account on biglab. You will almost definitely crash your laptop if you try to work locally, unless you have a $!@#-ton of RAM, so now is as good a time as any to learn how to read, write, and run code from the command line! Bonus, we already have the data on biglab for you, so you don't need to download it. It is in the directory <code>/home1/n/nets213/data/</code>. You can look at the files in a directory by typing <code>ls</code> (for "list"). E.g.

	<pre><code>$ ssh epavlick@biglab.seas.upenn.edu
	epavlick@biglab.seas.upenn.edu's password: 
	SEAS SuSE Linux 13.1
	epavlick@big05:~> ls /home1/n/nets213/data
	training-data unlabelled-data</code></pre>

	You should see two directories, one containing your training data (this is the same as last week) and one containing unlabelled data. The unlabelled data is in two parallel files: <code>articles.txt</code> contains the text of the articles that you will use for the classifier. <code>urls.txt</code> contains the urls from which this text came; you will use these in Part 2 of the assignment.

2. You will the use the same classifier you built last week, but this time, instead of testing it with cross validation and priniting out the accuracy, you will train it on all your labeled data, and then use it to make predictions on your unlabelled data. To do this, download our [new code template](http://www.seas.upenn.edu/~epavlick/nets213/predict_unlabelled.py) (the easiest way would be to use [wget](https://www.gnu.org/software/wget/manual/html_node/Simple-Usage.html#Simple-Usage)!). This code should look very familiar to what you worked with last week, but has a few new functions added, which will handle the reading and vectorizing of the unlabelled data. The only change you will need to make is to <b>replace the <code>get_features()</code> function with the <code>get_features()</code> function that you wrote</b> last week. If you used any auxilary functions as part of your <code>get_features</code>, you will need to copy those over too.  

	You can copy over your function, and if you are careful, it should run without complaining. (Note: To give you an idea of the main changes that needed to be made in order to have the classifier work on new data, read through the comments in the main method. Specifically, look at the function <code>get_matricies_for_unlabelled()</code>. The main difference is that when we convert our feature dictionary into a feature matrix, we need to make sure we use the same <code>DictVectorizer</code> object that we used to create the training data. This makes sense- we need to make sure that the column 627 in our new matrix means the same thing as column 627 in the training matrix, otherwise, the classifier will be totally helpless! You can also look at the function <code>predict_unlabelled()</code>. This should look very similar to the function you wrote to pull out misclassified examples in the homework last week.)

3. Once you have copied over your feature function, you can run the program as follows. 

	<pre><code>$ python predict_unlabelled.py /home1/n/nets213/data/training-data/articles.txt /home1/n/nets213/data/unlabelled-data/articles.txt</code></pre>

	You might want to test your code to make sure it works before running on the full 1.5M articles, so try running with just a few lines of data/unlabelled-data/articles.txt. You can do this by giving the code a third argument, e.g. to predict for the first 10 articles, run

	<pre><code>$ python predict_unlabelled.py /home1/n/nets213/data/training-data/articles.txt /home1/n/nets213/data/unlabelled-data/articles.txt 10</code></pre>

	This will still take a few minutes, since you still need to train on all 70K training articles! 

	If it works, run on the full 1.5M articles. Once you start it, don't hold your breadth. Maybe go grab coffee...or a nice dinner downtown...go for a leisurly hike. It took me about 20 minutes to finish on biglab. When the code finishes, it will have created a file called <code>classifier_predictions.txt</code>, which contains the classifier predictions, one per line. E.g. the first line of <code>classifier_predictions.txt</code> is a '0' if the classifier thinks that the first article in data/unlabelled-data/articles.txt is not gun related. My classifier found a little under 190,000 articles that it thought were gun-related. You can check this with the bash command we mentioned in class: 

	<pre><code>$ cat classifier_predictions.txt | sort | uniq -c </code></pre>.

4. You now have three parallel files, each with 1,471,811 lines in it: <code>unlabelled-data/articles.txt</code>, <code>data/unlabelled-data/urls.txt</code>, and <code>classifier_predictions.txt</code>. For the next step, you will want to pull out just the urls of the articles which the classifier predicted as "gun-related"- that is, the lines for which classifier_predictions.txt has a '1'. You can use your favorite programming language to do this, or do it manually if you are bored and have nothing better to do. If you are interested, here is a great bash command to do it for you: 

	<pre><code>$ paste classifier_predictions.txt /home1/n/nets213/data/unlabelled-data/urls.txt | grep -e "^1" > positive_predicted_urls.txt</code></pre>

	This creates a new file, positive_predicted_urls.txt, with two columns, one with the label (which will always be '1'), and one with the url. It uses three bash commands: <code>paste</code> just takes the contents of both files and pastes them side-by-side; <code>grep</code> searches for lines which match the pattern <code>^1</code>, where the <code>^</code> just means "beginning of the line"; and the "<code>></code>" symbol (often read as "redirect") tells it to put the output into a new file, called <code>positive_predicted_urls.txt</code>.

5. Finally, you will need to get a sample of these articles to label on Crowdflower. We will label 500 positive predictions. Again, some bash to the rescue:

	<pre><code> $ cat positive_predicted_urls.txt | shuf | head -500 > sample.txt</code></pre>
	
	This creates a new file, <code>sample.txt</code> which contains a random 500 lines from <code>positive_predicted_urls.txt</code>. Again, it uses three bash commands: <code>cat</code> (for "concatenate") just dumps the entire contents of a file; <code>shuf</code> scrambles the order of the lines; <code>head -n</code> takes the top <code>n</code> lines of its input and ignores the rest. 


###Part 3: ShootingsHIT

Whew, okay, enough python and bash for now! Its time to design a HIT on Crowdflower! The goal is to have the workers look at each of the URLs you gathered in step 4 of Part 1, and have them judge whether they agree that it is gun-violence-related. This should be a very painless process, hopefully. And look! There are even pictures!

1. Prep your data. You will need the list of urls to be in CSV format. The easiest way to do this will probably be to open <code>sample.txt</code>, or whatever you called your file, in a spreadsheet program like Google Docs. Then, you can use File->Dowload as->CSV, and save the file. Make sure you add a header to the columns, something informative like "url" or "stuff." 

2. Log onto [Crowdflower](https://crowdflower.com/). Click on "Your Jobs" -> "Create New Job." Then choose "Start from scratch."

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

	Once the results are in, you can download them as a CSV file from the dashboard. Answer the few quick questions [here](https://docs.google.com/forms/d/10QW0B9xAZK2q9AISGJmYjs7QE3awx3f9h1meypUW5NU/viewform) about your results. We will do more work analyzing the results (specifically, the worker's quality) in the coming assignments.


The deliverables are: 
	
1. Your <code>classifier_predictions.txt</code>, which should be a 1,471,811 line file, containing precitions (0 or 1) for each unlabelled article.
2. The final, labeled data you get from Crowdflower, as a csv file.
3. A screenshot of your HIT, as it looked to workers.
4. Your responses to [these questions](https://docs.google.com/forms/d/10QW0B9xAZK2q9AISGJmYjs7QE3awx3f9h1meypUW5NU/viewform). 

Like before, please turn in your files using turnin:
<pre><code>$ turnin -c nets213 -p crowdflower -v *</code></pre>

This assignment is due <b>Wednesday, October 1</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment.  
