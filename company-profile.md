---
layout: default
img: Crowdsourcing_Landscape
img_link: http://www.thinketc.com/wp-content/uploads/2012/05/Crowdsourcing_Landscape.jpg
title: Company profile presentation
active_tab: company-profile
---

Company Profile
=============================================================
As part of your [market research assignment](assignment2.html), you will give a short 5 to 10 minute presentation on your company.  Your presentation should answer the following questions:

- What incentives does the company offer to get people to participate?
- How does it aggregate the information provided by the crowd?
- What are the quality concerns, and how does the company do quality control?
- How does the company benefit from user contributions?

You will do research on the company, and [fill out a questionnaire about the company](https://docs.google.com/forms/d/1cEkW2h2xwVyKaXriKR7PqroPDjQZE34AKPoRP-lUV5Y/viewform?usp=send_form) by <b>Wednesday, September 10</b>. See the HW description for more details.

Your TA will give an example presentation to illustrate what we’re looking for. 

Here are some companies that you could profile:
[538](http://fivethirtyeight.com),
[99Designs](http://99designs.com),
[airbnb](https://www.airbnb.com),[ALEC](http://www.alec.org/model-legislation/) ,
[ALICE](http://alicelaw.org),
[Amazon reviews/product recommendations](https://www.amazon.com),
[Book Country](http://www.bookcountry.com),
[Buy Amazon Reviews](http://www.buyamazonreviews.com),
[change.org](https://www.change.org),
[coursera](https://www.coursera.org),
[CrowdFlower](http://www.crowdflower.com),
[CrowdMed](https://www.crowdmed.com),
[EatWith](http://www.eatwith.com),
[eBay buyer/seller ratings](http://pages.ebay.com/help/feedback/scores-reputation.html),
[edX](https://www.edx.org),
[Flattr](https://flattr.com),
[Foursquare](https://foursquare.com),
[Freebase](http://www.freebase.com),
[Freelancer](https://www.freelancer.com/),
[Iceland’s Crowdsourced Constitution](http://www.slate.com/articles/technology/future_tense/2014/07/five_lessons_from_iceland_s_failed_crowdsourced_constitution_experiment.html),
[IndieGoGo](https://www.indiegogo.com),
[Innocentive](http://www.innocentive.com),
[Instacart](https://www.instacart.com/faq),
[iStockPhoto](http://en.wikipedia.org/wiki/IStock),
[Intrade](http://en.wikipedia.org/wiki/Intrade),
[Iowa Election Markets](http://tippie.uiowa.edu/iem/),
[Kaggle](http://www.kaggle.com),
[Kickstarter](http://www.kickstarter.com),
[Kiva](http://kiva.org),
[Lending Club](https://www.lendingclub.com/public/how-peer-lending-works.action),
[Lyft](https://www.lyft.com),
[MTurk List](http://www.mturklist.com),
[Netflix recommendations](https://www.netflix.com/),
[ODesk](https://www.odesk.com),
[OpenStreetMap](http://www.openstreetmap.org/),
[Parchment](http://www.parchment.com)
[PatientsLikeMe](http://www.patientslikeme.com),
[Prosper](https://prosper.com/welcome/how_it_works.aspx),
[PublicStuff](https://www.publicstuff.com),
[Quirky](http://quirky.com),
[Quora](http://www.quora.com),
[Rotten Tomatoes](http://www.rottentomatoes.com),
[Samasource](http://samasource.org),
[Silk Road](http://arstechnica.com/tech-policy/2014/08/dark-net-drug-markets-kept-alive-by-great-customer-service/),
[Stackexchange](http://stackexchange.com/sites),
[Stackoverflow](http://stackoverflow.com) ,
[TaskRabbit](https://www.taskrabbit.com),
[Threadless](https://www.threadless.com/how-it-works/),
[Thumbtack](http://www.thumbtack.com/),
[topcoder](http://www.topcoder.com),
[TurkOpticon](http://turkopticon.ucsd.edu),
[Uber](https://www.uber.com),
[Udacity](https://www.udacity.com),
[Ushahidi](http://www.ushahidi.com),
[Waze](https://www.waze.com),
[We the People](https://petitions.whitehouse.gov),
[Wikipedia](http://en.wikipedia.org/wiki/Main_Page),
[XPRIZE](http://www.xprize.org),
[Yelp](http://www.yelp.com/)

The Freakonomics podcast had an interesting [episode about the sharing economy](http://freakonomics.com/2014/09/04/regulate-this-a-new-freakonomics-radio-podcast/), which discussed some of these companies. 

For full details about the assignment, [check out homework page](wa2.html).


<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date</th>
      <th>Company Profile</th>
    </tr>
    {% for company in site.data.companies %}
   <tr>
      <td>{{ company.date | date: "%b %d" }}</td>
      <td>
	Company Profile:  
        {% if company.slides %}<a href="{{ company.slides }}">{{ company.title }}</a>
        {% else %}{{ company.title }}{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 