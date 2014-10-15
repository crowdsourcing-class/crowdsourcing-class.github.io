---
layout: default
img: information_overload1
caption: Love the information age...
title: Homework 6 | Crowdsourcing IE
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 22nd.</div>


Crowsourcing Information Extraction<span class="text-muted"> : Assignment 6</span> 
=============================================================

Okay, so we've been talking all semester about this gun violence database. And we've been making all sorts of big promises to Doug and the other epidemiologists. But, what have we gotten so far: "Here are some articles that we are about 10% confident are about guns. Also, the word "shooting" is a good feature." Not exactly anything to write home about. So time to deliver. Let's take these articles and turn it into something useful. 

We will do this using (surprise!) crowdsourcing. This week, you are going to ask Crowdflower workers to read through the articles that you all identified as gun related back in homework 5, and pull out the key facts in a principled way. Your primary goal is to design an interface that helps them do this quickly and accurately. We will walk you through some initial steps to get you started on the design, but you are welcome to go in your own direction.  

Your deliverables will be:
1. Two csv files from Crowdflower containing the information the workers extract
2. Screen shots of your two HIT designs
3. Reponses about your findings in [this questionnaire](https://docs.google.com/forms/d/1_qW91g5FDIS5qa_2TdKtlfkMQDggT8b7QbuhFJ-0f08/viewform?usp=send_form).

You will might want to work in teams for this porject. These HITs will require more time for the crowd workers, and so should pay a bit more than the previous ones. Don't be a jerk and pay them pennies just because your account is low! Buddie up with someone, or feel free to add some funds to your account. (We didn't have a text book for this class, remember? So we've been easy on your budget so far.)

###Code, data, and signing up for more emails

1. In assignment 5, you guys had workers label your classifier's results. To give you data to work with, we've pulled together 200 of the urls your workers called "gun related." We've also written some code to do some text processing for you, which we will talk about in a few steps. You can download all the code and data [here](). 

	<pre><code> $ wget assignment6.tgz
	$ tar -xvzf assignment6.tgz
	$ ls assignment6/
	clean_and_process_data.py	convert_to_csv.py		gun-violence-urls.txt</code></pre>

2. You should see three files. `gun-violence-urls.txt` contains 198 urls that your workers labeled as gun-related in the previous assignment. `clean_and_process_data.py` is a script which will perform basic text processing to clean up your articles and help pull out some potentially useful information (like names and locations). <code>convert_to_csv.py</code> will put your data into a csv that can be uploaded to Crowdflower. 

3. In order to do the text processing, we will be using the [Alchemy API](http://www.alchemyapi.com/api/calling-the-api/). This is a super awesome professional API which does a lot of very complicated NLP for you and makes it seem easy. You should play around with their [online demo](http://www.alchemyapi.com/products/demo/alchemylanguage/). Specifically, look at the text extraction and entity extraction features, since these are the main features we will use. 

	In order to use Alchemy, you will need to [sign up for an account](http://www.alchemyapi.com/api/register.html) and get an API key. The default account will give you 1,000 API calls a day. This is probably enough for this assignment- you will need two calls per url, so if you only mess up one and a half times, you should still be within your daily limit. However, if you want to explor it more (which you really should! its awesome!) you can sign up for an academic account, which will give you 30,000 calls a day. If you want to do this, let me know. It just requires sending an email to the sales team, and you can copy the email I used to request my academic license.

###HIT Design

As you may remember from [Doug's lecture](http://crowdsourcing-class.org/slides/gun-violence-as-a-public-health-issue.pdf), there are a lot of details about gun crimes that epidemiologists are interested in. For this assignment, you are going to ask workers to try to extract the following information: 

- Time and place
	- City
	- State
	- Additional fine-grained location information 
	- Date
	- Time of day
- Detials about shooter(s) (may have to answer questions multiple times if multiple victims)
	- Number of shooters
	- Name
	- Gender
	- Age
	- Race
- Detials about victim(s) (may have to answer questions multiple times if multiple victims)
	- Number of victims
	- Name
	- Gender
	- Age
	- Race
	- Killed? 
	- Injured?
	- Hospitalized? 
- Circumstances of shooting
	- Type of gun
	- Number of shots fired
	- Was it a case of domestic violence?
	- Did the ictim and shooter know each other?
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

####Not very good design

1. First, we will design a simple HIT. You can see my simple version [here](https://tasks.crowdflower.com/assignments/10fc01e8-201e-41d5-b315-b55cf136e6ed). You do not have to follow my designs exactly, but your design should extract the same information.

2. From assignment 5, you should all be familiar with how to use the crowdflower interface. You should use <code>gun-violence-urls.txt</code> as your input data (remember you will need to add a header row!); in the next design, you will have to use an input with some more columns, but for now, you only need the urls.

3. Just because this is the "simple HIT design" doesn't mean it should be a UI monstrosity. Crowdflower has a pretty cool [custom markup language]() which gives you some nice control over how your questions are displayed. You might want to consider using something like the "only-if" field, so that workers don't have to view questions about victims number 2,3,4, and 5 if there is only one victim in the article. For example, I used this code so that the "Name of victim #2" question only appears if the worker answered that there are 2 or more victims. 
	
    <pre><code> &lt;cml:select label="Number of shooters" validates="required"&gt;
    &lt;cml:option label="1" id=""/&gt;
    &lt;cml:option label="2" id=""/&gt;
    &lt;cml:option label="3" id=""/&gt;
    &lt;cml:option label="4" id=""/&gt;
    &lt;cml:option label="5 or more" id=""/&gt;
    &lt;/cml:select&gt;
    ...
    &lt;cml:text label="Shooter #2 name" only-if="number_of_shooters:[2]||number_of_shooters:[3]||number_of_shooters:[4]||number_of_shooters:[5]" validates="required"/&gt;</code></pre>

####Less bad design

4. Now, we will use Alchemy to design a nicer HIT interface, which will hopefully allow your workers to move through the articles more quickly and accurately. You can see my design [here](https://tasks.crowdflower.com/assignments/7062734c-e446-41c6-b491-90ba89165fb2). Again, you are encoraged to improve over my template! I am a god-awful web designer, so please! Make it better so we can recycle your designs for next year's students! :-P 

5. To do this, we will use Alchemy's [text extraction]() to display the cleaned-up text to the workers. We will also use Alchemy's [entity extraction](http://www.alchemyapi.com/api/entity-extraction/), [date extraction](http://www.alchemyapi.com/api/publication-date/), and [keyword extraction](http://www.alchemyapi.com/api/keyword-extraction/). Open `clean_and_process_data.py`. This script will make the API calls using python. You can see how the API calls are constructed by looking at the request strings at the top of the file. 

	<pre><code>http://access.alchemyapi.com/calls/url/URLGetText?apikey=[KEY]&url=[URL]&outputMode=json</code></pre>

	We will make two calls, one to extract the text, and one [combined call]() which will extract the remaining information. The file reads from "standard input", which you can run the program by doing the following:

	<pre><code>python clean_and_process_data.py &lt; gun-violence-urls.txt</code></pre>

	This will write the results to a file called `gun-violence-urls-and-entitites.csv`.

6. You will need to put the extracted data into a csv format, so that Crowdflower can understand it. The `convert_to_csv.py` script will do this for you. If you open it up, you will see that it reads through the extracted list of entities for each article and wraps them in an html `&lt;span&gt;` tag, so that you can handle them specially when you are designing your interface. Running the following will create a file called `gun-article-info.csv` that Crowdflower should understand. 
	
	<pre><code> python convert_to_csv.py gun-violence-urls-and-entitites.csv </code></pre>

7. Take another shot at your interface design, now taking advantage of the fact that you have a fairly good (but not perfect) list of the people and places in the article. You are welcome to reimpliment my design, although there is lots of room for improvement. Check the extra credit opportunities for more ideas! 

This assignment is due <b>Wednesday, October 22</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment. 

####Extra credit

If you like web design, awesome! We are completely willing to give extra credit for faster, simpler, and sexier UIs. A few ideas:
- Pre-populate answers to the form so users can simply confirm or edit the answers.
- Allow users to click on entities in the text and flag them as specific fields (e.g. "victim") withough having to type into the text boxes.
- Anything with drag and drop. People love to drag and drop.
- Alchemy does a good job, but misses some important things like dates and times. Try some other tools to detect this, or write your own!

####Very useful hints

1. If you want to launch your HIT so that only you can do it (to test it without paying workers), go to "Contributors" and then to the "Channels" tab, and turn off "On-Demand Workforce." Then you can follow the link at the bottom of the dashboard to test your own HIT. 

2. Don't use javascript! Use [jQuery](http://jquery.com/). Javascript is an ugly nightmare, jQuery is small and sleek and beautiful. If you don't know javascript, don't bother learning. Just use jQuery. 

3. If you want to include jQuery in your HIT, you can do this in Crowdflower's javascript editor. You can see it by clicking the "Show Custom CSS/JS" link at the buttom of the "Build Job" page. However, if you want to access the data fields in your csv from your javascript, you will need to include the javascript within the CML editor. Here is the javascript I included to show/hide groups of questions in my HIT. You can add this to the top of your CML editor and use it as a template for your own HIT.

	<pre><code>
	&lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js">&lt;/script&gt;
	&lt;script type="text/javascript" charset="utf-8"&gt;
	document.addEvent('domready', function(){
	try {
    		require(['jquery-noconflict','bootstrap-modal','bootstrap-tooltip','bootstrap-popover','jquery-cookie'], function($) {
		Window.implement('$', function(el, nc){return document.id(el, nc, this.document);});
		var $ = window.jQuery;
				
		/*My code. Everything else is stuff that makes Crowdflower happy.*/
		$('#timeandplace').hide();
		$('#timeandplacebar').click(function(e){
			$('#timeandplace').toggle();
		});
		});
	} catch(e) {
		console.log('ERR: '+e)
	}
	});
	&lt;/script&gt;

