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

<!-- MathJax -->
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>


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

##Part 1: Majority vote
    
q_i = \frac{\sum_{t \in \text{tweets}[i]} \delta(l_{ti} == \text{majority}[t])}{|\text{tweets}[i]|}

##Part 2: Weighted majority vote

##Part 3: The EM algorithm

	

<!--3. Open <code>majority&#95;vote&#95;template.py</code>. You will need to provide a few lines of code to complete the logic in the two methods metioned above. The comments in the code should help you but, in the spirit of EM, I will reiterate:

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
-->
