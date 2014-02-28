---
layout: default
img: quality-never-goes-out-of-style
caption: Quality never goes out of style.
title: Homework 6 | EM Algorithm
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 23rd.
</div>


EM Algorithm<span class="text-muted">: Programming Assignment 4</span> 
=============================================================
Last week, we used the embedded quality controls in order to determine how to approve and reject workers. This week, we will continue with the quality-control theme, but with a slightly different perspective. Now, we want to try to figure out how 'good' that data is. Is it good enough to train a sentiment classifier in the next assignment? Or did you waste all of your hard-earned-free-Amazon-money on utter crap? 

We will attempt to answer two questions:

1. How good are the labels I received? How do I combine the (likely conflicting) labels from multiple Turkers in order to accurately label my data?
2. How good are my workers? Which workers are reliable and which ones appear to be lazy and/or inebriated?

In class, we have discussed three different quality estimation methods to answer these questions:

1. Embedded controls (What you did last week) : A label is considered 'correct' if the Turker who provided it correctly answered the embedded gold standard question. Note that, using this method, we can get more than one 'correct' label for the same tweet. Based on the data and the application, this may or may not be a property that you want.
2. Majority vote : A label is considered 'correct' if it agrees with the majority, i.e. matches whatever is most popular. This is an intuitive algorithm, widely used among insecure adolescents.* 
3. [Expectation maximization](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) : A label's 'correctness' is determined using an iterative algorithm, which uses the estimated quality of the worker in order to infer the labels, and then the estimated labels in order to infer the quality of the worker. This algorithmic framework is one of the favorites of machine learning and NLP, and we will cover it in more detail in the lecture. For this assignment, we will use Panos Ipeirotis' implementation, [Project Troia](http://project-troia.com/).

*<font size="1px">(Alternatively, although we will not be implimenting it, one could conceive of an algorithm which always chooses the least popular answer, just to be different. See [Hipster](http://www.urbandictionary.com/define.php?term=hipster) and [Too Cool for School](http://www.urbandictionary.com/define.php?term=Too%20Cool%20for%20School&defid=4468945).)</font>

For this assignment, you will run all three algorithms and provide a brief analysis comparing their differences.

##TO DO

1. As in previous assignments, we will provide you with code and ask you to fill in a few lines of the logic in order to run the algorithms. Download our code <a href="downloads/assignment_4.tar.gz">here</a>, and unzip the tarball. 
	$ tar -xvzf assignment_4.tar.gz
    You will see six files. The ones denoted 'template' are the ones that you will have to edit. As a brief overview of the files:
    <code>label&#95;map.py</code> : Should look familiar from last assignment - a mapping of the labels that you used in your HIT to standard labels.

    <code>majority&#95;vote&#95;template.py</code> : Majority vote quality estimation
    
    <code>embedded&#95;control&#95;.py</code> : Embedded control quality estimation. You will not need to edit this file since you did this last week.
    <code>troia&#95;em&#95;template.py</code> : EM quality estimation using Troia server .
    
    <code>quality&#95;estimation.py</code> : Combines the estimates from the above three algorithms, and outputs aggregated CSV files for analyzing.

    <code>analysis&#95;template.py</code> : Runs some basic analysis to compare differences in the algorithms
	
Each of the three algorithm files (<code>majority&#95;vote&#95;template.py</code>, <code>embedded&#95;control.py</code> , and <code>troia&#95;em&#95;template.py</code>) implements two methods, <code>estimate&#95;data&#95;labels()</code> and <code>estimate&#95;worker&#95;qualitites()</code>, which do exactly what they sound like they should do (I debated naming them <code>method&#95;1()</code> and <code>method&#95;2()</code> but my proper programming training got the best of me), but differ slightly based on the algorithm. You will be responsible for completing this methods in <code>majority&#95;vote&#95;template.py</code> and completing a small piece in <code>troia&#95;em&#95;template.py</code>. 

2. Open <code>label&#95;map.py</code> and fill in your labels, the same way you did in the previous assignment.

3. Open <code>majority&#95;vote&#95;template.py</code>. You will need to provide a few lines of code to complete the logic in the two methods metioned above. The comments in the code should help you but, in the spirit of EM, I will reiterate:

    <code>estimate&#95;data&#95;labels()</code> : Here, you simply need to return a dictionary mapping each tweet to its most popular label.

    <code>estimate&#95;worker&#95;qualities()</code> : Here, you need to return a dictionary mapping each worker to their accuracy against the most popular label. I.e. in math, the quality of worker i, $q_i$, is 
	
    $$q_i = \frac{\sum_{t \in \text{tweets}[i]} \delta(l_{ti} == \text{majority}[t])}{|\text{tweets}[i]|}$$

    where tweets$[i]$ is the set of all the tweets labeled by worker $i$, $l_{ti}$ is worker $i$'s label for tweet $t$, majority$[t]$ is the most popular label for tweet $t$, and $\delta(x)$ evaluates to 1 if $x$ is true. 

	Okay, there that is. We've met our quota for overly-mathifying very simple concepts. CS classes must do this at minimum once per semester in order to reassure the engineering school that we are sufficiently rigorous.

4. Open <code>embedded_control.py</code>. Verify that this looks similar to what you did in the last assignment. The functions will be slightly different:

    <code>estimate&#95;data&#95;labels()</code> : In this case, we are accepting <i>all</i> labels from a HIT if the control tweet in that HIT was labeled correctly. This means that, unlike before, we may accept multiple labels for the same tweet. Therefore, we return a dictionary mapping each tweet to a set of accepted labels.

    <code>estimate&#95;worker&#95;qualities()</code> : Again we return a dictionary mapping each worker to their accuracy against the controls. I'm going to mathify again, because I just spent 30 minutes downloading <a href="http://www.mathjax.org/">MathJax</a> over a very slow Starbucks network, so I want to use it for more than one equation. 

	$$q_i = \frac{\sum_{h \in \text{hits}[i]} \delta(c_{hi} == \text{gold}[c_{h}])}{|\text{hits}[i]|}$$

	where hits$[i]$ is the set of all the hits in which worker $i$ participated, $c_{hi}$ is worker $i$'s label for the control tweet in hit $h$, gold$[c_h]$ is the gold standard label for the control tweet in hit $h$, and $\delta(x)$ evaluates to 1 if $x$ is true. 

	That equation was <i>totally</i> unnecessary, but look how pretty it looks with that $\sum$ and that $\delta$. So worth it.

5. Open <code>troia&#95;em&#95;template.py</code>. You will need to fill in a few lines to estimate the worker accuracies, marked in the file. I also suggest that you look through the code and make sense of what's going on. From an engineering standpoint, if you are not familiar with python's <a href="http://docs.python.org/2/library/urllib2.html">urllib2</a> or <a href="http://docs.python.org/2/library/json.html">json</a> modules, it is worth your time familiarizing yourself with them. From an theoretical standpoint, EM is a very important algorithmic framework. If you are interested in machine learning and want to get deeper into the mathematics of EM, check our <a href="../resources.html">resources</a> page for pointers to some good online introductions. Or you can just plunge straight into the mathy mathness of the <a href="../readings/downloads/ml/EM.pdf">original paper</a> on which Troia is based.

6. Once you've finished filling in the necessary functions from the above steps, you can run <code>quality&#95;estimation.py</code>, passing it the path to your HITs CSV:


     <code>$ python quality&#95;estimation.py hits.csv</code>

     This will run all three algorithms, and produce two CSV files, <code>data&#95;quality&#95;estimates.csv</code>, which contains the predicted data labels from each algorithm for each tweet, and  <code>worker&#95;quality&#95;estimates.csv</code>, which contains the predicted worker qualities from each algorithm for each worker. Sometimes, if your network is shotty, the EM code might give an error like <code>KeyError : 'result'</code>. This just means your Troia server didn't respond normally, and should work if you just try it again. (Computers, amiright? Think how much easier this class would be without them...)

7. Open <code>analysis&#95template.py</code>. This will read in the output from <code>quality&#95;estimation.py</code> and output some summarization analysis. You need to fill in a few lines (marked in the file) in order to compute the overall accuracy of the data, according to the label predictions made by each algorithm. The program will make use of <a href="http://matplotlib.org/">matplotlib</a>. Directions for installing it are <a href="http://matplotlib.org/users/installing.html">here</a>. You can also run it on eniac. (I tried and it works for me. Make sure you use <code>$ ssh -X you@eniac.seas.upenn.edu</code>. If you forget the <code>-X</code>, you will not be able to use the graphics environment necessary to produce the figures.)

8. Run 
    <code>$ python analysis&#95;template.py</code>

This will give you 1) a graph comparing the estimated overall data accuracy, according to each algorithm and 2) a graph of each worker's estimated quality according to each algorithm. Use these to answer the following questions:
	
  * What was your accuracy a) against the majority vote? b) against the controls? c) against the EM estimated labels? Why do the estimates differ? What are some of the weakness of each approach?
  * How does each algorithm rank your workers? Do they agree on which workers are most/least trustworthy? 
	
9. Finally, open <code>troia&#95;em.py</code> again, and uncomment the code block around line 40. This will seed the EM algorithm with your gold data. Reproduce the graphs (you might want to go into the code and change the names that they are saved as, so you don't overwrite your first graphs). Answer the following question:

  * How is EM different when you seed it with gold data? Does it agree more or less with the other algorithms?

10. Turn in your code, your two pairs of graphs and a few paragraphs. (!!)
