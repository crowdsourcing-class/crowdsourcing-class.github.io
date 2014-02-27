---
layout: default
img: raised-fist
caption: Workers of the world, unite!
title: Homework 5 | Quality never goes out of style
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 2nd.
</div>


Quality never goes out of style<span class="text-muted">: Programming Assignment 2</span> 
=============================================================
The original plan for this week was for you to automatically grade your Turkers by checking the control tweets you embedded and rejecting the workers who failed to match your answer. There were a few problems with this. Primarily : we didn't want to make you do two assignments in one week, but Turkers are not nearly patient enough to wait two weeks for their payments. So we are reworking the assignment. (Of course, not until after I had completely designed the old assignment. Way to incentivize procrastination, world...). Instead you will run a few 'what-if' scenarios and analyze the tradeoffs. Next week, we will go into more depth and look at quality control mechanisms that do not use embedded controls. 

If you haven't already done so  : <b>approve your workers!</b> They are sitting at home, twiddling their thumbs, waiting for their money.

Approval and rejection of workers is done in three ways. You will probably use (or have already used) the website's 'Approve all' button, which is fine for this assignment. If you wanted to run the grading scripts from this assignment and acutally approve/reject based on the results, you could do so by communicating with MTurk via CSV files, similar to the way we created the HIT. For more heavy-duty MTurking, you can use the [API](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ApproveAssignmentOperation.html) to approve and reject HITs. 

##TO DO

<ol>
<li>If you haven't downloaded all of your data yet, do that now. Hopefully you all have 1000 annotated tweets. You can go to the <code>Manage</code> tab of your requester account. Next to the name of your batch of HITs, click on <code>Results</code> and then on <code>Download CSV</code>.

<br><br>

<li>Download the <a href=downloads/pa3.tar.gz>code for this assignment</a> and unzip it. If you are <a href="http://xkcd.com/1168/">not sure</a> how to do this on the command line:

	<ul>
	<li><code>$ tar -xvzf pa3.tar.gz</code> 
	</ul>

You will see three files. The ones denoted 'template' are the ones that you will have to edit. As a brief overview of the files:
	
	<ul>
	<li><code>grade&#95;hits&#95;naive&#95;template.py</code> : Grading script which approves or rejects each HIT based only on the control tweet in that HIT.
	<li><code>grade&#95;hits&#95;moresmarter&#95;template.py</code> : Grading script which approves or rejects each HIT based on the average performance of each worker. 
	<li><font size="1%">(My fiance was voted 'most smartest' by his high school classmates. The title was completely sincere and endorsed by the faculty. I don't think grammar was a top priority in that school's curriculum...)</font>
	<li><code>analysis.py</code> : Very short script to compile results.
	</ul>

<li> Open <code>grade&#95;hits&#95;naive&#95;template.py</code>. There are a few lines that need to be completed in order for you to run the script, and they are marked with 'TODO'. All this script needs to do is check each control tweet against the gold standard answer and determine whether the Turker answered correctly. The script should then put an <code>'X'</code> in either the <code>Approve</code> or <code>Reject</code> column of the CSV. 

<br><br>

<li> When you think your script is working, run it by passing it the path to your downloaded data. E.g.

	<ul>
	<li><code>$ python grade&#95;hits&#95;naive&#95;template.py hits.csv</code> 
	</ul>

<li> Open the output file, <code>hits&#95;graded&#95;naive.csv</code>. Double check by spot checking some of the approvals and rejections and verifying that you agree with the decisions your script made. 

<br><br>

<li> The grading method you just implemented works, but it seems a little unfair. You saw for yourselves that labels on tweet sentiment are hardly cut and dry. Many workers could make an honest effort, but still miss a few of the controls. A better approach might be to remember how well each worker is doing. This way, for workers that have done well in the past, we can allow a little leeway if they miss a control. Similarly, for workers who have done a bad job historically, we can assume that even on a HIT where they get the correct label on the control, their work is probably not worth keeping. Open <code>grade&#95;hits&#95;moresmarter&#95;template.py</code>. 

In this script, we will implement the protocol <a href="../slides/being-an-mturk-requester.pdf">described in class</a> (see slide 53). We will define three parameters : 
<br><br>
	<ul>
	<li><code>FREE_HITS</code> : Number of HITs to approve 'for free' from each worker. This allows us to get a representative sample from the worker before we start making judgements about the quality of their work.
	<li><code>REJECT_THRESHOLD</code> : Value that accuracy score must be below in order for us to assume the worker is consistantly bad. A typical way to chose this is to set it to the accuracy that could be acheived by random chance.
	<li><code>APPROVE_THRESHOLD</code> : Value that accuracy score must be above in order for us to assume the worker is consistantly good. This depends on your mood.
