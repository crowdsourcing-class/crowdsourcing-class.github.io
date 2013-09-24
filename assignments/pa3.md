<ul id="ProjectSubmenu">
    <li><a class="home" href="../index.html" title="Home">Home</a></li>
    <li><a class="syllabus" href="../syllabus.html" title="Lectures">Lectures</a></li>
    <li><a class="assignments" href="../assignments.html" title="Assignments">Assignments</a></li>
    <li><a class="resources" href="../resources.html" title="Resources">Readings</a></li>
</ul>

<link rel="stylesheet" type="text/css" href="../stylesheet.css" />

# Crowdsourcing and Human Computation

##Programming Assignment 3 : Due Wednesday, October 2

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
	</ul>
We will then classify workers into one of four categories
<br><br>
	<ul>
	<li><code>PREAPPROVE</code>: Worker has not yet used up their free hits, so we approve them blindly
	<li><code>BLOCKED</code> : Worker has completed more than <code>FREE_HITS</code> hits, and their accuracy is below <code>REJECT_THRESHOLD</code>. We reject them for the rest of their life.
	<li><code>TRUSTED</code> : Worker has completed more than <code>FREE_HITS</code> hits, and their accuracy is above <code>APPROVE_THRESHOLD</code>. We accept them for the rest of their life.
	<li><code>PENDING</code> : Worker has completed more than <code>FREE_HITS</code> hits, but has not yet hit either of our thresholds. We approve or reject them proportional to their accuracy on the controls.
	</ul>

Most of your work will be in maintaining the data structure to keep track of which category a worker is in. You will see the 'TODOs' in the file. Don't overthink it; most of these only require one line of code. 

Once these categories are known, the logic is very simple. See the pseudocode below. We will simulate this whole process in a streaming style, meaning that we will look at the HITs one at a time, make our updates, and then approve or reject before seeing the next HIT. This means that if a worker were to fall into <code>BLOCKED</code> status in their first 10 HITs, and then bounce back, we would continue to reject their work. This is a natural way to process the HITs since, in a real-world setting, you often do not have all the data available from which to make your decisions. 

<code>
<ul>
<li> for each HIT : 
	<ul>
	<li>update worker status to include their performance on this HIT
	<li>if worker.status == '<code>PREAPPROVE</code>' : Approve HIT
	<li>else if worker.status == '<code>BLOCKED</code>' : Reject HIT
	<li>else if worker.status == '<code>TRUSTED</code>' : Approve HIT
	<li>else if worker.status == '<code>PENDING</code>' : Approve if control is correct, reject otherwise
	</ul>
</ul>
</code>

<li> When you think your script is working, run it by passing it the path to your downloaded data. E.g.

	<ul>
	<li><code>$ python grade&#95;hits&#95;moresmarter&#95;template.py hits.csv</code> 
	</ul>

<li> Open the output file, <code>hits&#95;graded&#95;moresmarter.csv</code>. Double check by spot checking some of the approvals and rejections and verifying that you agree with the decisions your script made. 

<br><br>

<li> Finally, run the analysis. This will just pring out how many approvals and rejections you made under each of the methods. 

	<ul>
	<li><code>$ python analysis.py</code> 
	</ul>

<li> For your writeup, play around with the different parameters and see what conclusions you can draw. Choose a few different thresholds for <code>FREE_HITS</code>, <code>REJECT_THRESHOLD</code> and <code>APPROVE_THRESHOLD</code>, and run <code>analysis.py</code> again. How much of a difference does each of the parameters make on your approval rate? What if you change the leniency with which you consider a control to be correct? (I.e. If you call a control 'positive', do you consider a worker correct if they call it 'strongly positive' or 'neutral'?). Spot check some approvals and rejections - do they seem fair to you? How should you decide on values for these thresholds? What are some of the positives and negatives of this form of quality control? Can you think of ways to extend the algorithm? Please submit your code, and a short paragraph of analysis answering these questions. You don't have to answer all the questions explicitly, but say something interesting, hopefully unique to your data, and include some numbers. I need to see that you looked at the results and thought about them, and that you didn't just code-monkey your way through implimenting the algorithms, but I have a fairly low <code>REJECT_THRESHOLD</code>. Ooof, bad joke. Good sign I should stop.

</ol>


 
