<ul  id="ProjectSubmenu">
    <li><a class="home" href="index.html" title="Home">Home</a></li>
    <li><a  href="syllabus.html" title="Lectures">Lectures</a></li>
    <li><a class="assignments" href="assignments.html" title="Assignments">Assignments</a></li>
    <li><a class="resources" href="resources.html" title="Resources">Readings</a></li>
</ul>

<link rel="stylesheet" type="text/css" href="stylesheet.css" />

# Crowdsourcing and Human Computation

## Topics on the syllabus

###August 28 : [Intro Lecture](slides/class-intro.pdf)
- Relationship between crowdsourcing, human computation, collective intelligence, data mining, social computing
#####Reading
	- "The Wisdom of Crowds" Chapter 0 - Introduction
	- "The Wisdom of Crowds" Chapter 1 - The Wisdom of Crowds
	- ["Harnessing Crowds: Mapping the Genome of Collective Intelligence"](readings/downloads/intro/MaloneEtAl.pdf) by researchers out of MIT and Boston University
	- The [Wired article](readings/downloads/intro/Wired.pdf) which coined the phrase "Crowdsourcing"

###September 4: [The Mechanical Turk crowdsourcing platform - part 1](slides/amazon-mechanical-turk.pdf)
- Working on Mechanical Turk, demographics of Mechanical Turk workers, estimating the size ofthe Mechanical Turk Marketplace
- Terminology and mechanics: Turkers, Requesters, HITs, micropayments
####Reading
	- "The Wisdom of Crowds" Chapter 2 - The Difference Difference Makes
	- [Analyzing the Amazon Mechanical Turk Marketplace](readings/downloads/platform/Ipeirotis.pdf)
	- [The Demographics of MTurk](readings/downloads/platform/demographics-of-mturk.pdf)

###September 9: [The Mechanical Turk crowdsourcing platform - part 2](slides/being-an-mturk-requester.pdf)
- Amazon Mechanical Turk from the Requester's perspective: Designing HITs, qualifications, pricing HITs, approving/rejecting
####Reading
	- "The Wisdom of Crowds" Chapter 3 - Monkey See, Monkey Do
	- [Requester Tour of Mechanical Turk](https://requester.mturk.com/tour}
	- [Mechanical Turk blog](http://mechanicalturk.typepad.com/blog/requester/)


###September 11: [Taxonomy of crowdsourcing and human computation](slides/taxonomy-of-human-computation.pdf)
- Categorization system: motivation, quality control, aggregation, human skill, process flow
####Reading
	- "The Wisdom of Crowds" Chapter 4 - Putting the Pieces Together
	- ["Human Computation: A Survey and Taxonomy of a Growing Field"](readings/downloads/intro/QuinnAndBederson.pdf) by researchers out of University of Maryland
	- [Worker Evaluation in Crowdsourcing: Gold Data or Multiple Workers?](http://www.behind-the-enemy-lines.com/2010/09/worker-evaluation-in-crowdsourcing-gold.html), Panos Ipeirotis' blog post estimating the quality of workers. 

###September 16: [Programming concepts for human computation](slides/programming-the-crowd.pdf)
- People as function calls, decomposing complex tasks into simpler subtasks
- Memoizataion of expensive function calls, "Crash and Re-Run"
- [Quicksort for kittens](slides/quicksort-with-kittens.mov)
####Reading
	- "The Wisdom of Crowds" Chapter 5 - Shall We Dance?
	- ["TurKit: Human Computation Algorithms on Mechanical Turk"](readings/downloads/programming/Turkit.pdf)
	- [Download the TurKit software from the MIT Computer Science and Artificial Intelligence Laboratory](http://groups.csail.mit.edu/uid/turkit/)

###September 18: [Experiments with TurKit](slides/iterative-and-parallel-processing.pdf)
- Programming language with MTurk built in
####Reading
	- [Exploring Iterative and Parallel Human Computation Processes](readings/downloads/programming/LittleEtAl.pdf), by researchers out of MIT and University of Washington. (This paper wins the prize for the best quote : "We considered other puzzle possibilities, but were concerned that they might be too fun.")

###September 23: [Crowdsourcing and human computer interaction (HCI) design](slides/crowdsourcing-and-HCI.pdf)
- Next generation interfaces 
- Soylent word processor ("it's made of people")
####Reading
	- "The Wisdom of Crowds" Chapter 8 - Science
	- [Soylent : A Word Processor with a Crowd Inside](readings/downloads/hci/Soylent.pdf), a plugin for MS Word which allows users to have their work edited by Turkers.
	- [VizWiz: Nearly Real-time Answers to Visual Questions](readings/downloads/hci/Vizwiz.pdf), an app which uses MTurk to help blind people with simple tasks, like finding matching socks or reading the nutrition labels.

###September 25: [Crowdsourcing and HCI part 2 - privacy and latency]()
- E-mail Valet
- Adrenaline
####Reading
	- [Crowds in Two Seconds: Enabling Realtime Crowd-Powered Interfaces](readings/downloads/hci/adrenaline.pdf)
	- [EmailValet: Managing Email Overload through Private, Accountable Crowdsourcing](readings/downloads/hci/EmailValet.pdf)
	- [VizWiz: Nearly Real-time Answers to Visual Questions](readings/downloads/hci/Vizwiz.pdf), an app which uses MTurk to help blind people with simple tasks, like finding matching socks or reading the nutrition labels.



###Upcoming: [The economics of crowdsourcing]()
- Pricing HITs, incentivizing Turkers
- Ensuring high quality data, balancing cost and quality
####Reading 
	- "The Wisdom of Crowds" Chapter 10 - The Company
	- "The Wisdom of Crowds" Chapter 11 - Markets
	- [Financial Incentives and the "Performance of Crowds"](readings/downloads/econ/MasonAndWatts.pdf)
	- [Cheap and Fast - But is it Good?](readings/downloads/econ/SnowEtAl.pdf), about the using non-expert workers to collect expert-quality data.
	- [Get Another Label? Improving Data Quality and Data Mining Using Multiple, Noisy Labelers](readings/downloads/econ/ShengEtAl.pdf), about using redundant labeling to improve data quality and how to balance cost and quality


###Upcoming: [Crowdsourcing and machine learning]()
- Importance of labeled training data in ML, Computer Vision, Natural Language Processing
- Uses of crowdsourcing to reduce cost of ML, cost of expert annotations
- Uses of ML to reduce cost of crowdsourcing, EM algorithms for qualtiy estimation
####Reading
	- "The Wisdom of Crowds" Chapter 6 - Society Does Exist
	- "The Wisdom of Crowds" Chapter 7 - Traffic
	- [Maximum Likelihood Estimation of Observer Error-rates using the EM Algorithm](readings/downloads/ml/EM.pdf), the theory which is implemented by [Project Troia](http://project-troia.com/), which you will use in your assignment. This paper is math-heavy, but you all are a smart lot. [Believe in yourself.](http://virginiachepete.com/wp-content/uploads/2013/06/hey-you-can-do-it.jpg)
	- [CrowdFlow: Integrating Machine Learning with Mechanical Turk for Speed-Cost-Quality Flexibility](readings/downloads/ml/QuinnEtAl.pdf), describes a framework for using both computers and humans to label data
	- [Games with a purpose](readings/downloads/hci/GWAP.pdf), clever ideas for tricking people into having fun so you don't have to pay them to label your data.

###Upcoming: [Crowdsourcing and social science]()
- Experiments in linguistics, cognitive science, and political science
- Ethics of crowdsourcing
- How to apply for Institutional Review Board approval
####Reading
	- "The Wisdom of Crowds" Chapter 9 - Committees, Juries, and Teams
	- ["Running experiments on Amazon Mechanical Turk"](readings/downloads/platform/PaolacciEtAl.pdf), an overview of the MTurk platform, and the associated benefits and challenges
	- [Crowdsourcing User Studies With Mechanical Turk](readings/downloads/platform/KitturEtAl.pdf), about best-practices for designing tasks for a crowdsourcing environment.
	- [Citizen Science: Can Volunteers Do Real Research?](readings/downloads/social-science/Cohn.pdf), discussion of the ability of non-experts to collect scientific data.
	- [Mechanical Turk is not Anonymous](readings/downloads/social-science/LeaseEtAl.pdf), discusses a privacy vunerability in MTurk, and the implications for research ethics.
	- [Dirty Deeds Done Dirt Cheap](readings/downloads/social-science/Harris.pdf), discussion of some of the potentially malicious uses of crowdsourcing. Mostly included for the fantastically scathing title.
	- ["Gold Mine or Coal Mine?"](readings/downloads/social-science/FortEtAl.pdf), another fantastically scathing title...

###Upcoming: [Collective intelligence]()
- Surveying and polls, Prediction markets, A/B testing, Data mining
- Crowdfunding, product valuation, product reviews
####Reading
	- "The Wisdom of Crowds" Chapter 12 - Democracy
	- [Harnessing the Wisdom of Crowds in Wikipedia: Quality through Coordination](readings/downloads/collective-intelligence/Wikipedia.pdf). I now feel guilty for complaining about group projects with a group size of 3.
	- [Opinion Mining Using Econometrics: A Case Study of Reputation Systems](readings/downloads/collective-intelligence/GhoseEtAl.pdf), about using online reviews to predict the price differentials for products sold online.

###Company profiles (student presentations)
<ul>
<li>Platform providers: [Amazon Mechanical Turk](https://www.mturk.com/mturk/welcome), [oDesk](https://www.odesk.com/), [CrowdFlower](http://crowdflower.com/)</li>
<li>Creativity: [Threadless](http://www.threadless.com/), [iStockPhoto](http://www.istockphoto.com/), [99Designs](http://99designs.com/), [Book Country](http://www.bookcountry.com)</li>
<li>Reviews: [Amazon](http://www.amazon.com/) reviews, [Yelp](http://www.yelp.com/), [RottenTomatoes](http://www.rottentomatoes.com/), [Reddit](http://www.reddit.com/), [digg](http://digg.com/), [eBay](http://www.ebay.com/) buyer/seller rating system</li>
<li>Recommendations: [Netflix](https://signup.netflix.com/), [Amazon](http://www.amazon.com/) product recommendations, [LastFM](http://www.last.fm/), [Pandora](http://www.pandora.com/), [OKCupid](http://www.okcupid.com/)</li>
<li>Finance: [Kickstarter](http://www.kickstarter.com/), [Kiva](http://www.kiva.org/start)</li>
<li> Prediction Markets: [Iowa Electronic Markets](http://tippie.uiowa.edu/iem/), [Intrade](http://www.intrade.com/) (you can also read about its [fall from grace](http://en.wikipedia.org/wiki/Intrade)) </li>
<li> Social change: [Ushahidi](http://www.ushahidi.com/), [PatientsLikeMe](http://www.patientslikeme.com/), [crowdsourced patent review](http://www.forbes.com/sites/timworstall/2013/07/23/crowdsourcing-the-fight-against-bad-software-patents/) </li>
<li> Outsourcing knowledge work: [InnoCentive](http://www.innocentive.com/), [Freelancer](http://www.freelancer.com/), [SalesForce](http://www.salesforce.com/) </li>
</ul></li>


