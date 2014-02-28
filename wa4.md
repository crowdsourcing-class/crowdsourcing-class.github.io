---
layout: default
img: the-bottom-line
caption: Always remember the bottom line.
title: Homework 9 | Cost Analysis
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, December 4th.
</div>


Cost Analysis<span class="text-muted">: Assignment 9</span> 
=============================================================

Today is a very sad today. Your final homework assignment of the semester. The beginning of the end. I will greatly miss creating work for you all to do, as I know you will miss doing it. But for those of you who are not yet graduating and moving on to bigger and better things, take Machine Translation next semester (CIS 800/003)! I will not be TAing, but I will be taking it, so this is actually not shameless self-promotion.

Now, to the assignment. No coding this week. We want to take a step back and think about the big picture. What is this class _really_ about? 

Money, obviously. I don't just say that facetiously. You guys have all seen that crowdsourcing introduces a number of complications into your pipeline. And it is not as though turkers are the only people available to do your work for you. Honestly, if you want to pay $50 an hour for tweet labeling, you have my email. The reason people put up with all of the fuss of using MTurk (or any of the other crowdsourcing techniques we've discussed) is that it is [really damn cheap](http://www.youtube.com/watch?v=9s7CkbcSjBo).

But what exactly is "cheap"? How much data did your classifier require, and to reach what accuracy? How much more data would you need to get 10% better? 20% better? How much would this cost you?  This week, we want you to write a short analysis, roughly a page, discussing the costs of building your classifier and the projected costs of building a classifier that...you know...works.

Because you are the best and the brightest of America's college students, let's not just ponder the possible costs. Lets ground it in a bit of research and analysis. [Here](downloads/data-splits.zip) is the data from last week, spread over 10 files of increasing size (data.1.txt contains 10% of the data, data.5.txt contains 50%, etc). Run your classifier on each, and plot the learning curve. How much does an increase in training data help your accuracy? (FYI...yes, I cheated a bit. In this data set, we are using only three levels of sentiment (positive/neutral/negative). It makes the curve slightly nicer...)

Unfortunately, building a good classifier on this data turned out to be harder than I'd orginally hoped, so your learning curve might be less than enlightening for cost-analysis. That's okay - luckily many many others are working on the same problem. Check out a few of these papers ([here](downloads/pak-paroubek.pdf), [here](downloads/kouloumpis-et-al.pdf), [here](downloads/barbosa-feng.pdf), and also [here](downloads/stanford.pdf)) and see what kinds of accuracies others are reporting, and how much data they are using. (Note how many of them labeled the data themselves, or used labeling tricks like the presence of emotocons. Extra proof of the value of MTurk.) What would it cost to replicate their studies? To improve upon them?

Finally, think about the different components of your cost on MTurk. You labeled "gold data" yourself, for free, because we coerced you into it. But what if you had wanted to use embedded quality control and needed to hire a few students or "trusted" labelers to do it for at least minimum wage. What would be the cost? How much of your money was spent on collecting redundant annotations, rather than labeling new tweets? Think about Scott's lecture last Wednesday - to you think the cost of performing quality control is worth it? What are some more cost-efficient ways to ensure good quality work from Turkers? 

Compile your thoughts, and turn in a short writeup (~1 page text, extra space for figures always welcome). 


