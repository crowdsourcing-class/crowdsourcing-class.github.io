---
title: Crowdsourcing and Human Computation - NETS 213 - University of Pennsylvania
layout: default
img: turk-engraving-detail
img_link: http://en.wikipedia.org/wiki/The_Turk
caption: An engraving of the Mechanical Turk, the 18th century chess-playing automaton
active_tab: main_page 
---

Crowdsourcing and human computation are emerging fields that sit squarely at the intersection of economics and computer science. They examine how people can be used to solve complex tasks that are currently beyond the capabilities of artificial intelligence algorithms. Online marketplaces like [Mechanical Turk](https://www.mturk.com/) provide an infrastructure that allows micropayments to be given to people in return for completing human intelligence tasks. This opens up previously unthinkable possibilities like people being used as function calls in software. We will investigate how crowdsourcing can be used for computer science applications like machine learning, next-generation interfaces, and data mining. Beyond these computer science aspects, we will also delve into topics like the sharing economy, prediction markets, how businesses can capitalize on collective intelligence, and the fundamental principles that underlie democracy and other group decision-making processes.



<!--
<div class="alert alert-success" markdown="1">
[Use this form to rate your classmates' final presentations.](https://docs.google.com/forms/d/e/1FAIpQLSfYqCIPRVv6QKuD6qByilVLGPToMLN4Yr9yMBZfUVC8QYR5sQ/viewform?usp=sf_link)
</div>

<div class="alert alert-success" markdown="1">
[Please complete this end of semester survey.](https://docs.google.com/forms/d/e/1FAIpQLSeUh7fbELbIniQKyZ8DEapNo_7vM9fJiJmRWJCektpK_QEbcQ/viewform?usp=sf_link)
</div>

-->


<!--
<div class="alert alert-info">
<a href="https://docs.google.com/forms/d/e/1FAIpQLSd7Cw_J-dXQqT6mzGR9kZN3u6DSnVaLism2Z84SyyLUdIdbMw/viewform?usp=sf_link">How many jellybeans are in the jar?</a>
</div>

<div class="alert alert-info">
Are you a student who didn't get a permit, but you're still interested in enrolling the course? If so, <a href="https://docs.google.com/forms/d/e/1FAIpQLScHVWrUy3fupHdlaE4MDC5CTzXdq5ZIDrexwN8w6lUUU_AVoQ/viewform?usp=sf_link">please fill out this form</a>.
</div>
-->


<!--

<div class="alert alert-danger">
If you would like free credit on CrowdFlower, please sign up for <a href="https://make.crowdflower.com/users/new">a CrowdFlower account</a> and submit your details on <a href="https://docs.google.com/forms/d/1shp2S5Jl3r5bEx6hT_as8xQJZ5piiy2KRIEYQS_8U74/viewform">this Google form</a> before class on Wednesday. If you do not submit the Google form before Wednesday at 2pm, then you will not receive the free credit from CrowdFlower, and you will have to fund your account with your own money.
</div>

<div class="alert alert-danger" markdown="1">
Did you know you get participation credit for showing up in class?  During class today, we will pass out participation codes that you can enter into [this form](https://docs.google.com/forms/d/14UZWosW5_W_-qDNI8KJ_zUGkiyTO9yuwv7yCkCvuZgQ/viewform) to prove that you were there.
</div>

<div class="alert alert-info">
The first peer grading assignment is due on before class on Monday February 29th.  You will be grading your classmates' company profile videos.  Links to the videos were sent to you an email from nets213@seas.upenn.edu with the subject line "first peer grading assignment".
</div> 


<div class="alert alert-danger" markdown="1">
Did you know you get participation credit for showing up in class?  If you showed up the Friday before Spring break you're awesome and you get extra credit.  Write the code into [this form](https://docs.google.com/forms/d/15Ewt41aGE-muWdJHN6Qt_s8-K5p4Rs7voxvzeo3TQYI/viewform) to prove that you were there.
</div>


<div class="alert alert-info" markdown="1">
The second peer grading assignment is due on before class on Friday, March 25th.  You will be grading your classmates' pitches for their final projects.  Links to the videos were sent to you an email from nets213@seas.upenn.edu with the subject line "Final Project Pitch Peer Review Assignments". You can submit your feedback for the teams through [this form](http://goo.gl/forms/HzwsK9R5t7).
</div> 


<div class="alert alert-success" markdown="1">
Thanks for taking NETS 213!  Please help improve the course for next year by filling out [this Feedback Survey](https://docs.google.com/forms/d/1N926AFAjs97P7pS9rZ_BQeEUKZI1Yl98jfbZy1IuIws/viewform).
</div>

-->




<!-- Display an alert about upcoming homework assignments -->
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
{% for page in site.pages %}
{% if page.release_date and page.due_date %}
{% capture release_date %}{{page.release_date | date: '%s'}}{% endcapture %}
{% capture due_date %}{{page.due_date | date: '%s'}}{% endcapture %}
{% if release_date < now and due_date >= now %}
<div class="alert alert-info">
<a href="{{page.url}}">{{ page.title }}</a> has been released.  
{% if page.deliverables %}
The assignment has multiple deliverables.
{% for deliverable in page.deliverables %}
The {{deliverable.description}} is due before {{ deliverable.due_date | date: "%I:%M%p" }} on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.  
{% endfor %}
{% else %}
It is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
{% endif %}
</div>
{% endif %}
{% endif %}
{% endfor %}
<!-- End alert for upcoming homework assignments -->


<!--
<div class="alert alert-info" markdown="1">
Check out the [excellent final projects](http://crowdsourcing-class.org/final-projects-2016.html) from last year's class.
</div>
-->


Course number
: [NETS](http://nets.upenn.edu/) 213 - students from all majors are welcome!

Instructor
: [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/)

Teaching Assistants
: [Course Staff](staff.html) 

Website 
: [http://crowdsourcing-class.org/](http://crowdsourcing-class.org/)

Discussion Forum
: [Piazza](https://piazza.com/upenn/spring2021/nets213)

Time and place
: Spring 2021, Tuesdays and Thursdays 3-4:30pm Eastern [live via Zoom]( https://upenn.zoom.us/j/93824284661?pwd=OUNIQ2czUWRWTEQ3ZkRTU2FKQ3VGUT09)
: The first day of class will be Thursday January 21, 2021.
: The final day of class will be Thursday April 29, 2021.


Office Hours
: To join the office hour queue, please go to [OHQ.io](https://ohq.io/courses/204).
: Monday 10:30am-noon Eastern - Anna
: Monday 6pm-8pm Eastern – Ashley
: Tuesday 2pm-3pm Eastern - Bryan
: Wednesday 9:30am-11:30am Eastern - Zach
: Wednesday 1pm-3pm Eastern - Jason
: Wednesday 3pm-4:30pm Eastern - CCB
: Wednesday 7pm-9pm Eastern - Joe
: Wednesday 9pm-10pm Eastern - Sarah
: Thursday 8am-9:30am Eastern - Anka
: Thursday 9:30am-10:30am Eastern - Zach
: Thursday noon-2pm Eastern - Eddie
: Thursday 6pm-9pm Eastern - David
: Friday 10:30am-noon Eastern - Anna
: Friday 2pm-3pm Eastern - Bryan
: Friday 9pm-10pm Eastern - Sarah
: Saturday 10:30am-12:30pm Eastern - Megha
: Sunday 1pm-3pm Eastern - Ajay


Prerequisites
: [CIS 120](http://www.seas.upenn.edu/~cis120/) or prior programming experience.

Course Readings
: Each lecture has an accompanying set of [academic papers](lectures.html)

Grading
: This is a project-based course.  Instead of exams, you will do a series of hands-on assignments and a final project.  

* Weekly assignments (50%)
* Final project (45%)
* Participation (5%)


<!-- old grading 
This is a project-based course.  Instead of exams, you will do a series of hands-on assignments and a final project.  

* Weekly assignments (45%)
* Final project (45%)
* Peer grading (5%)
* Participation (5%)
-->

Late day policy
: Each student has ten free "late days". Homeworks can be submitted at most two days late. If you are out of late days, then you will not be able to submit your homework. One "day" is defined as anytime between 1 second and 24 hours after the homework deadline. 


Course materials
: Students should expect to spend around $50-$100 of their own money on MTurk or other crowdsourcing platforms.  If this will cause you undue financial hardship, please let the instructor know.

