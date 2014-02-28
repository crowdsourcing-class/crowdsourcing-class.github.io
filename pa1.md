---
layout: default
img: twitter
caption: Diverse tweets
title: Homework 2 | Twittering
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 11.
</div>


Twittering <span class="text-muted">: Programming Assignment 2</span> 
=============================================================
In this assignment, we will be collecting data from Twitter which we will use to train our sentiment classifiers. Scraping Twitter for news and sentiment data has become a huge deal for businesses and researchers, and not *just* because people care about [kittens](https://twitter.com/CatsPorn/status/367992670745927680/photo/1). Governments and academics are interested in whether Twitter and other [social media can reveal breaking news](http://homepages.inf.ed.ac.uk/miles/papers/short-breaking.pdf) before news networks can, and [many investors](http://www.sntmnt.com/), despite all [economic theory](http://en.wikipedia.org/wiki/Efficient_market_hypothesis), believe social media can help them beat the market. Being able to use Twitter data at scale is a great skill for graduating computer scientists and business-minded students, and not a bad starting point for those of you who want to get rich ([boost UPenn's ranking!](http://www.forbes.com/2008/05/19/billionaires-harvard-education-biz-billies-cx_af_0519billieu_slide_4.html)) and spend your 30s sipping cocktails on rooftop terraces.

We are providing you with code that makes it very easy to search Twitter for keywords and grab the ones you want, but we encourage you to play around with the code and extend it. We will be using [tweepy](http://pythonhosted.org/tweepy/html/index.html), which, like all python packages, is hosted on github, is well documented, and has a cutesy name involving 'py'. 	

1. Download and install tweepy from <a href="https://github.com/tweepy/tweepy">github</a>. If you have never installed code from github before, its very easy. Just open a terminal and run the following commands:

    $ git clone https://github.com/tweepy/tweepy.git

    $ cd tweepy

    $ sudo python setup.py install

    type pas$word123, or whichever other unhackable password you are using.

2. Download our <a href="downloads/get_tweets.py">script</a> for pulling data from Twitter using tweepy. (Courtesy of <a href="https://github.com/ryancotterell">Ryan Cotterall</a>, guru of all things python).

3. To run the script in the command line, use the following command where <code>n</code> is (optionally) the maximum number of tweets to grab and keywords are the words you want to search for. You must give at least one keyword. If you leave out the <code>n</code> parameter, you will continue to get tweets in a stream until you kill the program. 

    $ python get_tweets.py [n] keyword1 [keyword2 ... keywordn]


4. Collect 1000 tweets which reference a company of your choice.

    $ python get_tweets.py 1000 Apple > apple_tweets.txt 

Here are some example tweets I got by searching for 'Apple'. 

    * Using apple headphones on my galaxy s4 surely this must be a crime?     LSudeene

    * I'm dying. In the apple store there is some guys with a beer bong       kristinrutty

    * Smoking Near Apple Computers Creates Biohazard, Voids Warranty http://t.co/mVyy65Zn5W via @wordpressdotcom      TisOsama

    * RT @RudeComedian: I hate it when I'm wearing my apple bottom jeans and I can't find my boots with the fur.      emmilyy_b

    * Apple patent points to NFC on next iteration of the Apple iPhone and Apple iPad http://t.co/0S2OyY6HHb  yushadi_sy
 
    * RT @HonestToddler: I mean, Apple Juice is wonderful, but Apple Sauce? Room temperature smoothie in a bowl. Failure.	LT_Kbyrne

5. Download our <a href="downloads/convert_to_csv.py">script</a> to convert the Twitter output into a nice csv format. This script makes sure your data is in the format that MTurk expects, so that you can use it in the next assignment. Here, we use python's <a href="http://docs.python.org/2/library/csv.html">csv library</a> which is one you should definitely become comfortable with if you intend to do more large-scale data processing. It isn't difficult to convert into csv format by yourself, but using a library lets you avoid the little details, like escaping <a href="http://en.wikipedia.org/wiki/Comma-separated_values#Basic_rules_and_examples">special characters</a>, that are finicky and not particularly fun.

6. Convert your tweets into csv format using the below command. This will create a file called <code>tweets.csv</code>, which you can open in a spreadsheet program. Or in vim or emacs, if you are too hipster for spreadsheet programs, or if your computer is not <a href="http://i.imgur.com/3Fcper4.jpg">fancy enough for such things</a>. Note we use <code>shuf</code> to randomize the order of the tweets, because its good to randomize in research (i.e. good research is random...?). 

    $ cat apple_tweets.txt | shuf | python convert_to_csv.py 

7. Look at the first 100 tweets and manually label them for sentiment (positive, negative, or neutral). You will use your own labels later to check that Turkers are doing their work well (or at least as well as you are), so you should only label tweets that are fairly unambiguous. Skip over those that are very ambiguous, since it would not be fair to punish Turkers for disagreeing with you about labels of unclear or mixed-sentiment tweets. Remember, skipping over tweets is fine, but when you finish, <b>you need to have 100 tweets labled as either 'positive', 'negative', or 'neutral'.</b>

8. You only need to turn in <code>tweets.csv</code>, which should contain 1000 tweets, 100 of which are labeled. I.e. it should contain 1000 lines, 900 of which have two columns (tweet and user) and 100 of which have three columns (tweet, user, and label).  

