# Crowdsourcing and Human Computation
## Course ID: Special Topics CIS 399-001
## Class time: MW 4:30-6PM 
## Instructor: [Chris Callison-Burch](http://www.cs.jhu.edu/~ccb/)
## TA: [Ellie Pavick](http://www.seas.upenn.edu/~epavlick/)
## Course Website: [crowdsourcing-class.org](http://crowdsourcing-class.org)

# Course description
Crowdsourcing and human computation are emerging fields that sit squarely at the intersection of economics and computer science.  They examine how people can be used to solve complex tasks that are currently beyond the capabilities of artificial intelligence algorithms.  Online marketplaces like Mechanical Turk provide an infrastructure that allows micropayments to be given to people in return for completing human intelligence tasks. This opens up previously unthinkable possibilities like people being used as function calls in software.  We will investigate how crowdsourcing can be used for computer science applications like machine learning, next-generation interfaces, and data mining.  Beyond these computer science aspects, we will also delve into topics like prediction markets, how businesses can capitalize on collective intelligence, and the fundamental principles that underly democracy and other group decision-making processes.</p>

# Topics on the syllabus

* Taxonomy of crowdsourcing and human computation
	- Relationship between crowdsourcing, human computation, collective intelligence, data mining, social computing 
	- Categorization system: motivation, quality control, aggregation, human skill, process flow
* The Mechanical Turk crowdsourcing platform
	- Terminology and mechanics: Turkers, Requesters, HITs, micropayments
	- Designing good HITs
	- Decomposing complex tasks into simpler subtasks
* Programming concepts for human computation 
	- using people as function calls
	- memoizataion, parallel processing, iterative refinement
	- efficiently sorting pictures of kittens in order of cuteness
* Applications to human computer interaction (HCI) design 
	- next generation interfaces,  
	- the Soylent word processor ("it's made of people")
	- VizWiz an iPhone app for blind people
	- Games with a Purpose
* Applications to machine learning
	- importance of labeled training data in ML
	- Computer Vision, Natural Language Processing
	- cost-focused machine learning
* The economics of crowdsourcing
	- Demographics of Mechanical Turk
	- Analyzing the Mechanical Turk Marketplace
	- Ethics of crowdsourcing
	- Crowd funding 
* Crowdsourcing and social science
	- Experiments in linguistics, cognitive science, and political science
	- Is the Turker population representative of the general population?
	- Is the Turker population more or less representative than undergraduate Psych majors?
	- How to apply for Institutional Review Board approval
* Collective intelligence
	- Prediction markets
	- Surveying and polls
	- A/B testing
	- Data mining
* Company profiles (student presentations)
	- Platform providers: Amazon Mechanical Turk, oDesk, Crowdflower
	- Creativity: Threadless, iStockPhoto, 99Designs
	- Reviews: Amazon reviews, Yelp, RottenTomatoes, reddit, digg, eBay buyer/seller rating system
	- Recommendations: Netflix, Amazon product recommendations, LastFM, Pandora, OKCupid
	- Finance: Kickstarter, Kiva
	- Prediction Markets: Iowa Electronic Markets, in-trade
	- Social change: Ushahiti, PatientsLikeMe. crowdsourced patent review reform
	- Outsourcing knowledge work: InnoCentive, Freelancer, SalesForce

# Assignments and grading
Grades for the course will be based on weekly homework assignments and a final term project. The weekly homework will consist of a mixture of writing and programming assignments.  


## Programming assignments

You will complete a sequence of programming assignments that culminate in building a [Sentiment Analysis](http://en.wikipedia.org/wiki/Sentiment_analysis) system that will classify Tweets about companies as either positive, negative, or neutral.  Sample python code will be provided for many of the programming assignments.

- Sign up for a Requester account on MTurk
- Gather data from Twitter (turn in 1000 tweets that mention company X)
- Design a HIT
	- Create some gold standard items yourself
	- collect redundant labels
	- embed gold standard items alongside other data
- Write a script to grade the Turkers based on how well they do on your gold standard
	- Download the CSV results file and upload a graded CSV
	- Extra credit if you use the API 
- Quality control comparison 
	- majority vote
	- accuracy against gold standard
	- Run Panos's EM implementation
- Train a machine learning classifier on the annotated data that you collect
	- Extract Features 
	- Train a system
	- Evaluate it against held out gold standard

## Written assignments

- Sign up for MTurk as a worker, and write about your experience
	- Do 50-100 assignments
	- What tasks did you do, and how did you pick them?
	- How much money did you make?
	- What was your hourly wage per task?
	- How long did it take you to get paid?
	- Find tools for better Turking (Turkopticon, TurkerNation boards) 
- Write a synthesis of the academic papers
	- Choose one of the class topics
	- Read 3-5 of the academic papers in the optional reading for that topic
	- Write a synthesis of the academic papers
- Write a company profile
	- Pick a company that uses crowdsourcing in its business
	- Write a profile of it that describes how it uses crowdsourcing
		- What incentives does it offer to get people to participate?
		- How does it aggregate the information provided by the crowd?
		- What are the quality concerns, and how does the company do quality control?
		- How does the company benefit from user contributions?
	- Do a short in-class presentation about the company that you profiled
- Do Cost analysis of your Twitter sentiment classifer
	- Draw a learning curve
	- Estimate the cost of annotation to get to X% accuracy
	- What are the major components in the cost? (redundancy, embedded gold standard, etc)
	- How could you make it more efficient?


## Final project
The final term project will be a self-designed project created by the students in consultation with the professor and the TA.  Here are the guidelines for the final project.

- Should solve a real world problem
- Should actually use crowdsourcing (default: via MTurk)
- Should involve either an HCI or a ML component
- Should explain the choice of incentives and discuss alternative ways of incentivizing workers 
- Should contain a quality control component
- Analyze costs, decide whether it is a viable business
- Deliverables: 
	- midterm: proposal for project, selection of team, pitch to class, critique 
	- 2/3s of the way through: individual team meetings with TA+Prof, give concrete progress update
	- final: writeup and demonstration system
- Extra credit: 
	- lay the foundation for a PennApp 
	- use 99designs to create cool web site
	- Bonus Extra credit: start a business and put your Prof + TA on the board of advisors
	- Super extra mega credit: raise VC funding 
	- Loss of all credit: dropping out of school 



# Readings:
Selections from ["The Wisdom of Crowds" by James Surowiecki](http://www.amazon.com/The-Wisdom-Crowds-James-Surowiecki/dp/0385721706/), and various academic papers



