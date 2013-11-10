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
- Examples of crowdsourcing and human computation
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

###September 25: [Crowdsourcing and HCI part 2 - privacy and latency](slides/crowdsourcing-and-HCI-privacy-and-latency.pdf)
- E-mail Valet
- Adrenaline
####Reading
	- [Crowds in Two Seconds: Enabling Realtime Crowd-Powered Interfaces](readings/downloads/hci/adrenaline.pdf)
	- [EmailValet: Managing Email Overload through Private, Accountable Crowdsourcing](readings/downloads/hci/EmailValet.pdf)
	- [VizWiz: Nearly Real-time Answers to Visual Questions](readings/downloads/hci/Vizwiz.pdf), an app which uses MTurk to help blind people with simple tasks, like finding matching socks or reading the nutrition labels.

###September 30: [Quality Control - part 1](slides/quality-control.pdf)
- Agreement-based methods
- Embedded gold standard
####Reading
	- [Labeling Images with a Computer Game](readings/downloads/gwap/ESP.pdf)
	- [Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks](readings/downloads/nlp/evaluating-non-expert-annotations-for-nlp.pdf)

###October 2: [Quality Control - part 2](slides/quality-control-2.pdf)
- Reputation systems
- Economic incentives 
####Reading
	- [Opinion Mining Using Econometrics: A Case Study on Reputation Systems](readings/downloads/nlp/opinion-mining-using-econometrics.pdf)
	- [Financial Incetives and the Performance of Crowds](readings/downloads/econ/financial-incentives-and-the-performance-of-crowds.pdf)


###October 7: [Quality Control - part 3](slides/quality-control-3.pdf)
- The EM algortihm 
####Reading
	- [Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm](readings/downloads/ml/EM.pdf)
	- [Get Another Label? Improving Data Quality and Data Mining Using Multiple, Noisy Labelers](readinds/downloads/econ/get-another-label.pdf)


###October 15: [Machine Learning - part 1](slides/machine-learning.pdf)
- Examples of machine learning applications
- Naieve Bayes
- Text classification
####Videos
	- [Hilary Mason - Intro to Machine Learning in Python](http://shop.oreilly.com/product/0636920017493.do)

###October 21: [Machine Learning - part 2](slides/machine-learning-2.pdf)
- A high level perspective on how machine learning works and why it can fail
####Reading
	- [A Few Useful Things to Know about Machine Learning](readings/downloads/ml/useful-things-to-know-about-machine-learning.pdf)


###October 23: [Machine Learning - part 3](slides/machine-learning-3.pdf)
- Integrating machine learning and crowdsourcing
####Reading
	- [CrowdFlow: Integrating Machine Learning with Mechanical Turk for Speed-Cost-Quality Flexibility](readings/downloads/ml/CrowdFlow.pdf)



###October 28: [Distilling Collective Intelligence from Twitter - part 1](slides/twitter-first-story-detection.pdf)
- Topic Detection and Tracking
- Approximate alogriths for scaling to large data sets
####Reading
	- [Streaming First Story Detection with application to Twitter](readings/downloads/twitter/streaming-first-story-detection-with-application-to-twitter.pdf)
	- [Online Generation of Locality Sensitive Hash Signatures](readings/downloads/twitter/online-generation-of-locality-sensitive-hash-signatures.pdf)
	- [Approximate Nearest Neighbors: Towards Removing the Curse of Dimensionality](readings/downloads/twitter/approximate-nearest-neighbors.pdf)
	

###October 30: [Distilling Collective Intelligence from Twitter - part 2](slides/twitter-for-public-health.pdf) - Guest lecture by [Michael Paul](http://cs.jhu.edu/~mpaul/)
- Public health and Twitter
####Reading
	- [You are what you Tweet: Analyzing Twitter for Public Health](readings/downloads/twitter/analyzing-twitter-for-public-health.pdf)

###November 4: [Crowdsourcing and Human Subjects Research](slides/crowdsourcing-and-the-social-sciences.pdf)
- Is the Mechanical Turk population representative enough of the population to do social science experiments?
- Can we use Mechanical Turk to study clinical populations?
- Institutional Review Boards and human subject experiments
####Reading
	- [Amazon’s Mechanical Turk: A New Source of Inexpensive, Yet High-Quality, Data?](readings/downloads/social-science/perspectives-on-psychological-science.pdf)
	- [Using Mechanical Turk to Study Clinical Populations](http://cpx.sagepub.com/content/early/2013/01/31/2167702612469015.abstract)





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


