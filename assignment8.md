---
layout: default
img: quality-never-goes-out-of-style
caption: Quality never goes out of style.
title: Homework 8 | Quality control
active_tab: homework
---



<div class="alert alert-info">
  This assignment is due before class on Wednesday, November 5th.
</div>

Quality Control<span class="text-muted">: Assignment 8</span> 
=============================================================
As you all may have noticed, it is easy to get a lot of junk answers from Crowdflower. According to your workers, there are currently shooters on the loose with names like "3", "hi", "https://tasks.crowdflower.com/assignments/823118d2-af64-4c5e-b6f1-0510e2a2e659", and my personal favorite: ["felony"](http://freakonomics.com/2013/04/08/how-much-does-your-name-matter-a-new-freakonomics-radio-podcast/).

That being said, a lot of you actually go very good results. Before getting hung up on the various frustrating expereinces so many of you had, keep in mind the big picture. You are hiring anonymous workers from across the country (or world, if you forgot to set up your filters!), which Crowdflower recruits from ultra-sketchy sites like [this gem](http://www.clixsense.com/), and you are paying them a few cents for their time. I don't know about you, but based on all of my cynical models of human behavior, I would absolutely expect that you get 100% crap results back. But the truth is, you don't. You get a lot of really legitimate work from a lot of very sincere workers, you just need to make some effortto tease apart the good from that bad, which isn't always trivial. This is why we can dedicate a whole course to studying crowdsourcing, and its not a total waste of your Ivy League eduation. 

So, this week, we will attempt to answer two big questions:

1. How good are my workers? Which workers are reliable and which ones appear to be incompetent, lazy, and/or inebriated?
2. How do I combine the (likely conflicting) labels from multiple Turkers in order to accurately label my data?

In class, we have discussed three different quality estimation methods to answer these questions:

1. Majority vote: A label is considered 'correct' if it agrees with the majority, and all votes are equal. (Pure democracy!)
2. Confidence-weighted vote: A label is considered 'correct' if it agrees with the majority, but all workers are not equal. A worker's weight is proportional to their accuracy on your embedded gold-standard questions. (Elitist republic!)
3. [Expectation maximization](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) : A label's 'correctness' is determined using an iterative algorithm, which uses the estimated quality of the worker in order to infer the labels, and then the estimated labels in order to infer the quality of the worker. (Some new-fangled solution to politics...?)

For this assignment, you will run the first two algorithms and provide a brief analysis comparing them to eachother and to Crowdflower's super-secret quality estimation algorithm. We will work with the results of your first crowdflower task (the binary gun/not gun judgement HIT), since the algorithms are not designed for open-ended answers. You should think about ways to map these concepts onto the open-ended IE HIT you worked with last week.

Since EM is a more advanced algorithm, we will only require you to walk through a toy example. If you are interested in machine learning, and want to understand this concept better, you are welcome and encouraged to run it on your actual Crowdflower data. We will give you all the extra credit you could ever desire. Your name will be know all across Levine Hall.

##To Do

You will be using your own data from [Assignment 5](http://crowdsourcing-class.org/assignment5.html). You should download three reports: we will use the "Full" report for our own computations; we will use the "Aggregated" one and the "Contributors" one so that you can compare your own aggregation techniques against the ones used by Crowdflower.

##Part 1: Comparing aggregation methods

###Majority vote

Majority vote is probably the easiest and most common way to aggregate your workers labels. It is simple and gets to the heart of what "the wisdom of crowds" is supposed to give us- as long as the workers make uncorrelated errors, we should be able to walk away with decent results. Plus, as every insecure middle schooler knows, what is popular is always right. 

First, use majority vote to assign labels to each of the urls in your data. You can impliment it however you want, but will want to output <b>two-column, tab-separated file</b> in the format "url \t label". 

Lets call <i>u</i> a url and <i>labels</i> will be the dictionary that we build so <i>labels[u]</i> is the label we assign to <i>u</i>. Right now, we just have 

<p align="center" style="font-size:24px">
<i>labels[u]</i> = majority label for <i>u</i>.
</p>

Now, you will use the url labels to estimate a confidence in (or quality for) each worker. We will say that a worker's quality is simple the proportion of times that that worker agrees with the majority. 

Let's pull out some more notation, shall we? This is, after all, a CS class. We have a quota to meet for overly-mathifying very simple concepts, to give the illusion of principle and rigor. 

Lets call <i>qualities</i> the dictionary that we build to hold the quality of each worker. We'll call the <i>i</i>th worker <i>w<sub>i</sub></i> and we'll use  <i>urls[w<sub>i</sub>]</i> to represent all the urls for which <i>w<sub>i</sub></i> provided a label. We'll let <i>l<sub>ui</sub></i> to represent the label (e.g. "Gun-related", "Not gun-related", or "Don't know") that <i>w<sub>i</sub></i> assigns to url <i>u</i>. Then we calculate the quality of a worker as:

<p align="center" style="font-size:24px">
<i>qualities[w<sub>i</sub>]</i> = (1 / |<i>urls[w<sub>i</sub>]</i>|) * &Sigma;<sub><i>u</i> &isin; <i>urls[w<sub>i</sub>]</i></sub> &delta;(<i>l<sub>ui</sub> == labels[u]</i>)
</p>

Here, <i>&delta;(x)<i> is a special function which equals 1 if <i>x</i> is true, and 0 if <i>x</i> is false. 

Again, you should output a <b>two-column, tab-separated file</b> in the format "workerId \t quality".
    
### Weighted majority vote

Majority vote is great: easy, straightforward, fair. But should everyone really pull the same weight? As every insecure college student knows, whatever the smartest kid says is always right. So maybe we should recalibrate our voting, so that we listen more to the better workers. For this, we will use the embedded test questions that you created. We will calculate each worker's quality to be their accuracy on the test questions. E.g.  

<p align="center" style="font-size:24px">
<i>qualities[w<sub>i</sub>]</i> = (1 / |<i>gold_urls[w<sub>i</sub>]</i>|) * &Sigma;<sub><i>u</i> &isin; <i>gold_urls[w<sub>i</sub>]</i></sub> &delta;(<i>l<sub>ui</sub> == gold_label[u]</i>)
</p>

Once again, output a two-column, tab-separated file in the format "workerId \t quality". (Hint: you can see whether or not a row in your csv file corresponds to a gold test question by checking the "_golden" column.)

##Part 2: The EM algorithm

