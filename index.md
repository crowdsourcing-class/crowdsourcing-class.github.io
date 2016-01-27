---
title: Crowdsourcing and Human Computation - NETS 213 - University of Pennsylvania
layout: default
img: turk-engraving-detail
img_link: http://en.wikipedia.org/wiki/The_Turk
caption: An engraving of the Mechanical Turk, the 18th century chess-playing automaton
active_tab: main_page 
---

Crowdsourcing and human computation are emerging fields that sit squarely at the intersection of economics and computer science. They examine how people can be used to solve complex tasks that are currently beyond the capabilities of artificial intelligence algorithms. Online marketplaces like [Mechanical Turk](https://www.mturk.com/) and [CrowdFlower](https://crowdflower.com) provide an infrastructure that allows micropayments to be given to people in return for completing human intelligence tasks. This opens up previously unthinkable possibilities like people being used as function calls in software. We will investigate how crowdsourcing can be used for computer science applications like machine learning, next-generation interfaces, and data mining. Beyond these computer science aspects, we will also delve into topics like the sharing economy, prediction markets, how businesses can capitalize on collective intelligence, and the fundamental principles that underlie democracy and other group decision-making processes.


<div class="alert alert-info">
The class has reached its enrollment cap of 120 students.  You may <a href="https://docs.google.com/forms/d/1nEXV3LrZXckeOWiklEAKRYiCEJa-o67BbCEjAuOHuFw/viewform?usp=send_form">add yourself to the waitlist</a>, we will notify you if space becomes available. You are welcome to sit in on the lectures and start the homework assignments so that you don't fall behind.
</div>
 
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
The {{deliverable.description}} is due before class on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.  
{% endfor %}
{% else %}
It is due on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
{% endif %}
</div>
{% endif %}
{% endif %}
{% endfor %}
<!-- End alert for upcoming homework assignments -->

Course number
: [NETS](http://nets.upenn.edu/) 213 - students from all majors are welcome!

Instructor
: [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/)

Teaching Assistants
: [Course Staff](staff.html) 

Discussion Forum
: [Piazza](https://piazza.com/upenn/spring2016/nets213)

Time and place
: Spring 2016, MWF 2-3PM, LRSM Auditorium

Office Hours
: [See calendar page](calendar.html) 

Prerequisites
: [CIS 120](http://www.seas.upenn.edu/~cis120/) or prior programming experience

Course Readings
: Selections from [The Wisdom of Crowds by James Surowiecki](http://www.amazon.com/Wisdom-Crowds-James-Surowiecki-ebook/dp/B000FCKC3I/)
: [Various academic papers](lectures.html)

Grading
: This is a project-based course.  Instead of exams, you will do a series of hands-on assignments and a final project.  

* Weekly assignments (50%)
* Final project (40%)
* Peer grading (5%)
* Participation (5%)

Late day policy
: Everyone can have 5 free late days without penalty.  After you have used your free late days, you will lose 20% per day (or fraction thereof) that your assignment is submitted late. The final project will have its own late day policy.

Course materials
: CrowdFlower has generously provided each student with $100 credit on their platform.  Students should expect to fund their accounts with an additional $50-$100 of their own money.  If this will cause you undue financial hardship, please let the instructor know.

