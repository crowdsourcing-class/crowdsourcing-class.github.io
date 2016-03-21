---
layout: default
img: information_overload1
caption: Love the information age...
title: Homework 7 "Crowdsourcing Information Extraction"
active_tab: homework
release_date: 2016-03-21
due_date: 2016-03-27T14:00:00EST
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
  This assignment is due before class on Monday, March 27th.</div>


Crowdsourcing Information Extraction<span class="text-muted"> : Assignment 8</span> 
=============================================================

Okay, so we've been talking all semester about this gun violence database. And we've been making all sorts of big promises to Doug and the other epidemiologists. But, what have we gotten so far?: "Here are some articles that we are about 10% confident are about guns. Also, the word "shooting" is a good feature." Not exactly anything to write home about. So time to deliver. Let's take these articles and turn it into something useful. 

We will do this using (surprise!) crowdsourcing. This week, you are going to ask Crowdflower workers to read through the articles that you all identified as gun related back in Assignment 5, and pull out the key facts in a principled way. Your primary goal is to design an interface that helps them do this quickly and accurately. We will walk you through some initial steps to get you started on the design, but you are welcome to go in your own direction.  

Your deliverables will be:

1. Two csv files from Crowdflower containing the information the workers extract

2. Screen shots of two HIT designs (a bare-bones one, and a more user-friendly one).

3. Reponses about your findings in [this questionnaire](https://docs.google.com/forms/d/13ZPafIOfVTxco_Qa3YVYhK-gCC-aJwO-N20C3M3RNh0/viewform?usp=send_form).

You might want to work in teams for this project. These HITs will require more time for the crowd workers, and so should pay a bit more than the previous ones. Don't be a jerk and pay them pennies just because your account is low! Buddy up with someone, or feel free to add some funds to your account. (We didn't have a text book for this class. And we gave you each $50. So we've been easy on your budget so far.)

###Code, data, and signing up for more emails

1. <b>Download the code and data.</b> In Assignment 5, you all had workers label your classifier's results and came up with lists of crowd-approved gun-related articles. We've pulled together 400 of the urls your workers called "gun related" that you will use for this assignment. We've also provided some code templates for the text processing you'll need to do. You can download the code and data [here](http://crowdsourcing-class.org/assignments/downloads/assignment8.tgz). 

	<pre><code> $ wget http://crowdsourcing-class.org/assignments/downloads/assignment8.tgz
	$ tar -xvzf assignment8.tgz</code></pre>

2. <b>Familiarize yourself with the files.</b> You should see four files. `gun-violence-urls.txt` contains 100 urls that your workers labeled as gun-related in the previous assignment. `extract_text.py` and `extract_entities.py` are the scripts which you will edit to perform basic text processing using the Alchemy API. `convert_to_csv.py` is a script you will write mostly on your own to put your data into a csv that can be uploaded to CrowdFlower. 

3. <b>Sign up for the Alchemy API.</b> In order to do the text processing, we will be using the [Alchemy API](http://www.alchemyapi.com/api/calling-the-api/). This is a super awesome professional API which does a lot of very complicated NLP for you and makes it seem easy. You should play around with their [online demo](http://www.alchemyapi.com/products/demo/alchemylanguage/). Specifically, look at the text extraction and entity extraction features, since these are the main features we will use. 

	In order to use Alchemy, you will need to [sign up for an account](http://www.alchemyapi.com/api/register.html) and get an API key. The default account will give you 1,000 API calls a day. This is probably enough for this assignment- you will need two calls per url, so if you only mess up four times, you should still be within your daily limit. However, if you want to explore it more (which you really should! its awesome!) you can sign up for an academic account, which will give you 30,000 calls a day. If you want to do this, let me know. It just requires sending an email to the sales team, and you can copy the email I used to request my academic license.

###Extract Article Text using Alchemy API

We will use Alchemy twice: once (now) to extract clean text, and again (later) to extract entity and location names. We have code templates to do this, but you will need to modify them a little bit yourself.

1. <b>Construct an Alchemy API call to extract clean text from each URL.</b> We will use Alchemy's [text extraction](http://www.alchemyapi.com/api/text/urls.html#text) call. Open `extract_text.py`. This script should look similar to the code you used to call the Bing API in Assignment 5. You will need to modify the `construct_api_call` method to return a valid url request. The Alchemy API call for extracting text should look like this: 

	<pre><code>http://access.alchemyapi.com/calls/url/URLGetText?apikey=[KEY]&url=[URL]&outputMode=json</code></pre>
	
	Your final version of `extract_text.py` should read from [standard input](http://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29) and write to [standard output](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29). It should output two fields per line in tab-separated format: `url \t clean_text`. You should be able to run your script like this:
	
	<pre><code>cat gun-violence-urls.txt | python extract_text.py > gun-violence-urls-and-text.txt</code></pre>

###HIT Design

As you may remember from [Doug's lecture](http://crowdsourcing-class.org/slides/gun-violence-as-a-public-health-issue.pdf), there are a lot of details about gun crimes that epidemiologists are interested in. For this assignment, you are going to ask workers to try to extract the following information: 

- Time and place
	- City
	- State
	- Date
	- Time of day
- Detials about shooter (there many be multiple shooters, but we will only ask for information about one)
	- Name
	- Gender
	- Age
	- Race
	- Were there additional shooters? How many?
- Detials about victim (there many be multiple victims, but we will only ask for information about one)
	- Name
	- Gender
	- Age
	- Race
	- Killed? Injured? Hospitalized? 
	- Were there additional victims? How many?
- Circumstances of shooting
	- Type of gun
	- Number of shots fired
	- Was it a case of domestic violence?
	- Did the victim and shooter know each other?
	- Was the shooting during another crime (robbery, home invasion by the shooter, etc)?
	- Was the shooter attempting to deter a home invasion?
	- Was alcohol involved?
	- Were drugs involved?
	- Suicide or suicide attempt?
	- Inadvertent discharge of a firearm? 
	- Shooting by the police?
	- Shooting of a police officer?
	- Was the gun stolen?
	- Was the gun owned by the vitim or thier family?

You will design two HITs on Crowdflower to extract this information from the articles. In the first, you will simply provide the article and ask workers to fill in the information. In the second, you will do some preprocessing to try to make the workers' job easier. 

####Not very good design (Open-ended Inputs)

First, we will design a very simple HIT, in which we simply as workers to fill in the schema for us. You can see my simple version [here](https://tasks.crowdflower.com/assignments/74afb1ac-3e11-4487-b9ff-ddf5d6019eeb?cf_internal=true) (you might need to click the "start a new assignment" link). You do not have to follow my designs exactly, but your design should extract the same information.

1. <b>Prep your input csv.</b> From Assignment 5, you should all be familiar with how to use the crowdflower interface. You should use the <code>gun-violence-urls-and-text.txt</code> file that you just created as your input data (you might need to reformat the file and add a header row!).

2. <b>Design your interface.</b> Just because this is the "simple HIT design" doesn't mean it should be a UI monstrosity. Take the time to write clear instructions/examples. Crowdflower has a pretty cool [custom markup language](http://success.crowdflower.com/customer/portal/articles/1290342-cml-crowdflower-markup-language-) (or cml) which gives you some nice control over how your questions are displayed. Whether or not you decide to take advantage of the cml, it is worth skimming through the documentation so you know what is available.

3. <b>Post your HIT.</b> Once your simple HIT is to your liking, go ahead and post it.  

####Less bad design (Constrained Inputs)

The above HIT you designed is <i>very</i> open-ended. This makes it less work for you, but as you will probably see when the results come back, you pay for that convenience with the quality of the results you receive. As you probably noticed when doing the QC homework, there are a lot of benefits to having a constrained set of answers, so you can do things like take the majority vote, or measure agreement between workers. In this section, we will use Alchemy to design a nicer HIT interface, which will hopefully allow your workers to move through the articles more quickly and provide more consistent results. You can see my design [here](https://tasks.crowdflower.com/channels/cf_internal/jobs/887048/work?secret=jpRirnRaKlcoU%2BZxvWY0bAwR7j9VnBh%2B07agJaEHJ03l). You are encoraged to improve over my template! I am a god-awful web designer, so please! Make it better so we can recycle your designs for next year's students! :-P 


1. <b>Construct an Alchemy API call to extract entities from the article.</b>
We will also use Alchemy's [entity extraction](http://www.alchemyapi.com/api/entity-extraction/) and [date extraction](http://www.alchemyapi.com/api/publication-date/). This will allow us to design a more constrained interface so that workers hopefully give us more consistant inputs.

	We will use the Alchemy [combined call](http://www.alchemyapi.com/api/combined-call/) which will extract all of this information at once. The combined call you should use looks like this (it requests the article title, publication date, and a list of the entities in the article):
	
	<pre><code>http://access.alchemyapi.com/calls/url/URLGetCombinedData?apikey=%s&url=%s&extract=title,pub-date,entity&outputMode=json
</code></pre>
	
	You need to modify `extract_entities.py` in much the same way as you just did above. Again, your script should read from stdin and write to stdout. 

	<pre><code>cat gun-violence-urls-and-text.txt | python extract_entities.py > gun-violence-urls-and-text-annotated.txt</code></pre>
	
	The output of your script should again be tab-separated, and the fields should be: `url \t title \t publication_date \t clean_text \t entity_json`. The `entity_json` will be the string version of the [JSON](https://en.wikipedia.org/wiki/JSON) data structure that Alchemy returns to you. It should look like a list of dictionaries, like below. You will worry about processing the JSON in the next step.
	
	<pre><code>[{"relevance": "0.928925", "count": "2", "type": "Person", "text": "Stacey Craven"}, ... ]</code></pre>

3. <b>Convert your data to a CSV.</b> Now, you must complete `convert_to_csv.py` so that it reads in `gun-violence-urls-and-text-annotated.txt` and outputs a CSV file that CrowdFlower can understand. You can do the processing however you want, but we <i>highly</i> recommend using [Python's CSV module](https://docs.python.org/2/library/csv.html), [JSON module](https://docs.python.org/2/library/json.html), and [datetime module](https://docs.python.org/2/library/datetime.html). Taking the time up front to get comfortable with these modules will save you literally hours of time. You're CSV file needs to contain the following columns: 

	* url
	* tile
	* publication_date
	* person_1
	* person_2
	* person_3
	* person_4
	* person_5
	* city_1
	* city_2
	* city_3
	* city_4
	* city_5
	* text

	The `person_n` columns should contain the text associated with the first 5 `"type": "Person"` entities returned from Alchemy; the `city_n` columns should contain the text associated with the first 5 `"type": "City"` entities. If there are few than 5 Person/City entities returned, you should fill in as many columns as possible, and fill the remaining columns with the string `"--"`. 

	Your code should take one argument (the name of the input file) and output a single file called `crowdflower-input.csv`. I.e. running the command below should produce the `crowdflower-input.csv` file as specified.
	
	<pre><code> python convert_to_csv.py gun-violence-urls-and-entitites.csv </code></pre>
	
	<b>Hint</b>: In addition to recording the city and person names as columns in my CSV, I used the string `replace()` method to wrap the entity names in a `<span>` element whever they appear in `clean_text`. This allows me to highlight them easily in my HIT interface. 

4. <b>Redesign your HIT interface.</b> You will now redesign your HIT interface so that workers cannot input open-ended answers to your questions, but instead select from a pre-defined list of options. You will notice that this is not a perfect solution (Alchemy makes a lot of mistakes), but it solves many of the problems that arise with free text inputs. 

	At a minium, you should reimpliment [my design](https://tasks.crowdflower.com/channels/cf_internal/jobs/887048/work?secret=jpRirnRaKlcoU%2BZxvWY0bAwR7j9VnBh%2B07agJaEHJ03l), although there is lots of room for improvement. Check the extra credit opportunities for more ideas! 
	
5. <b>Post your HIT!</b> <- That! Do that! You should pay the same amount as you did for the previous step, so you can compare their cost and speed of the two designs.

###Extra credit

If you like web design, awesome! We are completely willing to give extra credit for faster, simpler, and sexier UIs. A few ideas:

- Collect information about all shooters/victims. Use CrowdFlower's markup language to dynamically add fields based on the number of shooters/victims. 
- Allow users to click on entities in the text and flag them as specific fields (e.g. "victim") withough having to select from the dropdown box.
- Alchemy does a good job, but misses some important things like dates and times. Try some other tools to detect this, or write your own!
- Anything with drag and drop. People love to drag and drop.

###Deliverables

Once again, your deliverables are:

1. Two csv files from CrowdFlower (one from the first HIT design, one from the second) containing the information the workers extract

2. Screen shots of each of your two HIT designs (a bare-bones one, and a more user-friendly one).

3. Reponses about your findings in [this questionnaire](https://docs.google.com/forms/d/13ZPafIOfVTxco_Qa3YVYhK-gCC-aJwO-N20C3M3RNh0/viewform?usp=send_form).

This assignment is due <b>Monday, March 27</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment. Remember to turn submit your questionnaire before the deadline. You can turn in your data and screenshots using turnin:

<pre><code>$ turnin -c nets213 -p crowdie -v *</code></pre>

<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This assignment is worth 5 points of your overall grade in the course.  The rubric for the assignment is given below.

* 1 point - CSV file containing data extracted using basic HIT design with open-ended inputs
* 1 point - CSV file containing data extracted using improved HIT design with constrained inputs
* 1 point - Screenshot of basic HIT design with open-ended inputs
* 1 point - Screenshot of improved HIT design with constrained inputs
* 1 point - Your completed [questionnaire](https://docs.google.com/forms/d/13ZPafIOfVTxco_Qa3YVYhK-gCC-aJwO-N20C3M3RNh0/viewform?usp=send_form).
* Extra credit (up to 1 point) - Your own UI improvements to the interface (you must turn in a screenshot and a short README describing the changes you made.)

</div>
</div>


<div class="panel panel-info" id="faq">
<div class="panel-heading" markdown="1">
#### Tips and FAQ
</div>
<div class="panel-body" markdown="1">

* How much should I pay?

	You should pay at least $0.05 per article. $0.10 would be better. You only have 100 urls to post, and each will be posted twice (once in each HIT design) so paying $0.10 will only cost you and your partner $20 combined. If this is an unmanageable finanical burden, please reach out to your professor or one of the TAs. 

* How many workers do I need to have work on each article?

	For this task, one worker per article is sufficient. Since everyone in the class is labeling the same URLs, there is no need for each group individually to collect redundant labels.

* Is it okay if I post few than 100 URLs? What if I get http/Alchemy errors and am not able to extract text from every URL? 

	That is okay, as long as you are not missing too many URLs. You should account for those that are missing by including a README with your submitted turnin files saying which URLs were skipped, and what errors they threw. Bad Gateway errors, for example, are okay. Errors that are due hitting your Alchemy API limit or due to bugs in your own code are not.

* Is there a way to launch my HIT so that I can debug it, without posting it "live"?

	Yes! If you want to launch your HIT so that only you can do it (to test it without paying workers), go to "Contributors" and then to the "Channels" tab, and turn off "On-Demand Workforce." Then you can follow the link at the bottom of the dashboard to test your own HIT. 

* JavaScript. What to do about it?

	If you want to build a fancier interface with any sort of interactive components, don't use javascript! Use [jQuery](http://jquery.com/). Javascript is an ugly nightmare, jQuery is small and sleek and beautiful. If you don't know javascript, don't bother learning. Just use jQuery. 

	If you want to include jQuery in your HIT, you can do this in Crowdflower's javascript editor. You can see it by clicking the "Show Custom CSS/JS" link at the buttom of the "Build Job" page. However, if you want to access the data fields in your csv from your javascript, you will need to include the javascript within the CML editor. 

</div>
