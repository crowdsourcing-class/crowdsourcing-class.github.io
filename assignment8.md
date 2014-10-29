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

1. First, use majority vote to assign labels to each of the urls in your data. You can impliment it however you want, but will want to output <b>two-column, tab-separated file</b> in the format "url \t label". 

Lets call <i>u</i> a url and <i>labels</i> will be the dictionary that we build so <i>labels[u]</i> is the label we assign to <i>u</i>. Right now, we just have 

<p align="center" style="font-size:18px">
<i>labels[u]</i> = majority label for <i>u</i>.
</p>

2. Now, you will use the url labels to estimate a confidence in (or quality for) each worker. We will say that a worker's quality is simple the proportion of times that that worker agrees with the majority. 

Let's pull out some more notation, shall we? This is, after all, a CS class. We have a quota to meet for overly-mathifying very simple concepts, to give the illusion of principle and rigor. 

Lets call <i>qualities</i> the dictionary that we build to hold the quality of each worker. We'll call the <i>i</i>th worker <i>w<sub>i</sub></i> and we'll use  <i>urls[w<sub>i</sub>]</i> to represent all the urls for which <i>w<sub>i</sub></i> provided a label. We'll let <i>l<sub>ui</sub></i> to represent the label (e.g. "Gun-related", "Not gun-related", or "Don't know") that <i>w<sub>i</sub></i> assigns to url <i>u</i>. Then we calculate the quality of a worker as:

<p align="center" style="font-size:18px">
<i>qualities[w<sub>i</sub>]</i> = (1 / |<i>urls[w<sub>i</sub>]</i>|) * &Sigma;<sub><i>u</i> &isin; <i>urls[w<sub>i</sub>]</i></sub> &delta;(<i>l<sub>ui</sub> == labels[u]</i>)
</p>

Here, <i>&delta;(x)<i> is a special function which equals 1 if <i>x</i> is true, and 0 if <i>x</i> is false. 

Again, you should output a <b>two-column, tab-separated file</b> in the format "workerId \t quality".
    
### Weighted majority vote

Majority vote is great: easy, straightforward, fair. But should everyone really pull the same weight? As every insecure college student knows, whatever the smartest kid says is always right. So maybe we should recalibrate our voting, so that we listen more to the better workers. 

3. For this, we will use the embedded test questions that you created. We will calculate each worker's quality to be their accuracy on the test questions. E.g.  

<p align="center" style="font-size:18px">
<i>qualities[w<sub>i</sub>]</i> = (1 / |<i>gold_urls[w<sub>i</sub>]</i>|) * &Sigma;<sub><i>u</i> &isin; <i>gold_urls[w<sub>i</sub>]</i></sub> &delta;(<i>l<sub>ui</sub> == gold_label[u]</i>)
</p>

Once again, output a two-column, tab-separated file in the format "workerId \t quality". (Hint: you can see whether or not a row in your csv file corresponds to a gold test question by checking the "_golden" column.)

4. You can use these worker qualities to estimate new labels for each of the urls in your data. Now, instead of a every worker getting a vote of 1, each worker's vote will be equal to their quality score. So we can tally the votes as 

<p align="center" style="font-size:18px">
<i>votes[u][l]</i> = &Sigma;<sub><i>w</i> &isin; <i>workers[u]</i></sub> &delta;(<i>l<sub>ui</sub> == l</i>) * <i>qualities[w<sub>i</sub>]</i>
</p>

where <i>votes[url][l]</i> is the weighted votes for assigning label <i>l</i> to url <i>u</i> and <i>workers[u]</i> just lists all of the workers who labeled <i>u</i>. Then 

<p align="center" style="font-size:18px">
<i>labels[u]</i> = <i>l</i> with max <i>votes[u][l]</i>
</p>

Output another file in the format "url \t label". 

###Comparing against Crowdflower

Crowdflower has its own way of aggregating worker votes and determining confidence it workers. They keep their exact algorithms locked up and secret, but you can see the results in the csvs you downloaded. The results of their <i>labels[u]</i> is just the labels assigned in the "Aggregated" report. You can see their confidence in each worker in the "Contributors" report. 

5. You can download [our script](assignments/downloads/cf_aggregation.py) to format their data for you. Run it as follows (passing it your aggregaed and contributor reports, respectively): 

	$ python cf_aggregation.py -d a621213.csv -m data > crowdflower_data.txt
	$ python cf_aggregation.py -d workset621213.csv -m worker > crowdflower_workers.txt

You should now have 6 files, 3 "url \t label" files and 3 "workerId \t quality" files. You will do some comparisons and report your findings in [this questionnaire](). 

6. First, we'll compare how well the three methods agree on what the "correct" label for each url should be. For this, we will use a metric called [Cohen's kappa](http://en.wikipedia.org/wiki/Cohen's_kappa), which attempts to measure the level of agreement between two sets of categorical labels. You can download [our script](assignments/downloads/kappa.py) for computing it, which you can run like this:

	$ python kappa.py crowdflower_data.txt majority_data.txt 
	kappa = 0.969854

To compare how well the three methods agree on the worker qualities, we will use [Kendall tau](http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient) correlation, which we talked about in class. Python has a [built-in implimentation](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.kendalltau.html) that you can use, or you can [impliment it yourself](http://en.wikipedia.org/wiki/Kendall_tau_rank_correlation_coefficient#Algorithms). Note that Python use's a slightly different definition than we discussed in class, so you might get different numbers depending on which method you decide to use. 

Your deliverables for this section are the 6 files you generated (3 "url \t label" files and 3 "workerId \t quality" files) and any code you used to generate them. Your code should be clearly named and reasonably commented. We will not need to run it, but we should be able to read it and see clearly what you did to generate your results. Remember to fill in the [questionnaire]().

##Part 2: The EM algorithm

The data aggregation algorithms you used above were straightforward and work reasonably well. But they are of course not perfect, and with all the CS researchers out there, all the Ph.Ds that need to be awarded and all the tenure that needs to be got, its only natural that many fancier, mathier algorithms have arisen. 

We discussed the expectation maximization (EM) algorithm in class as a way to jointly find the data labels <i>and</i> the worker qualities. The intution is "<i>If</i> I knew how good my workers were, I could easily compute the data labels (just like you did in step 4) and <i>if</i> I knew the data labels, I could easily compute how good my workers are (just like you did in step 3 above). The problem is, I don't know either." So our solution is to guess the worker qualities, use that to compute the labels, then use the labels we just computed to reassign the worker qualities, then use the new worker qualities to recompute the labels, and so on until we converge (or get bored). This is one of the best-loved algorithms in machine learning, and often appears to be somewhat magic when you first see it. The best way to get an intuition about what is happening is to walk through it by hand. So for this step, we will ask you do walk through XX iterations of EM on a [toy data set](assignments/downloads/em_toy_data.txt) and report your results in the [questionnaire](). 

You can refer to the [lecture slides](http://crowdsourcing-class.org/slides/quality-control-32.pdf) as a guide. The numbers are slightly different, but the process is idenitcal. If you are super ambitious, you are welcome to delve into the depths of the [original 1979 paper](http://crowdsourcing-class.org/readings/downloads/ml/EM.pdf) describing the use of EM for diagnosing patients. If you are super ambitious and/or super in want of extra credit, you can code it up and run EM on your own Crowdflower data!


##Deliverables

This assignment is due <b>Wednesday, November 5</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment. Remember to turn submit your questionnaire before the deadline.  Your deliverables are stated at the ends of parts 1 and 2, but in the spirit of EM, I will reiterate:

1. 3 files containing labels for each url, one file for each algorithm (majority, weighted, and crowdflower)
2. 3 files containing qualities for each worker, one file for each algorithm (majority, weighted, and crowdflower)
3. Your completed questionnaire 
4. Any code you used to run your algorithms and/or perform your analyses. Your code should be readable enough that we can tell what you did, but does not need to conform to any particular interface.

You can turn in your assignment using 

	$ turnin -c nets213 -p quality -v *
