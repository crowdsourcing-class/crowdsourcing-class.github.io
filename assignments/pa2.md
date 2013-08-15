<ul id="ProjectSubmenu">
    <li><a class="home" href="../index.html" title="Home">Home</a></li>
    <li><a class="syllabus" href="../syllabus.html" title="Syllabus">Syllabus</a></li>
    <li><a class="assignments" href="../assignments.html" title="Assignments">Assignments</a></li>
    <li><a class="resources" href="../resources.html" title="Resources">Resources</a></li>
</ul>

<link rel="stylesheet" type="text/css" href="../stylesheet.css" />

# Crowdsourcing and Human Computation

##Programming Assignment 2 : Due TBA 

This week, you will be using MTurk to label the data you scraped from Twitter in the last programming assignment. The theme of this assignment (and, really, the class) is quality. As you saw in your first assignment, MTurk tasks are usually simple and, yes, boring. Some turkers are lured in by the desire to strike it rich, two cents at a time, and will not pour their heart into giving you their highest quality work. Many other Turkers make a sincere effort, but can still make errors. Even if every Turker is perfectly reliable, we are dealing with a subjective question- classifying sentiment- and are guarenteed to get variation in the answers we recieve. In this assignment, we will address these issues in two ways:

<ul.circle>
<li>We will embed gold standard questions into the HITs (tweets with "known" sentiment), to check that Turkers are thinking about the tweets and not clicking randomly. 
<li>We will have multiple Turkers label each tweet, so that we can hopefully average away the subjective noise due to each individual Turker
</ul>

As you saw in lecture, there are many ways to attempt to control the quality of the data you receive from workers. There are several sites, [CrowdFlower](http://crowdflower.com/) and [ODesk](https://www.odesk.com/) to name a few, which differ from MTurk in that they enforce stricter quality requirements. In fact, CrowdFlower differentiates itself by doing exactly what we are going to do: embedding gold standard data into MTurk HITs. But we don't need no help from CrowdFlower. We will work within Mechanical Turk to get the quality standards we need all by ourselves. Like the ballers we are. 

For this assignment, we will be using MTurks online GUI interface to design our HITs and using CSV files to upload and download our data. Keep in mind that, should you want to use MTurk for more heavy-duty data processing in the future, there is an [API](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) which allows you much greater control over how your HITs operate. You can look into MTurk's [command line tools](http://aws.amazon.com/developertools/694), as well as the interfaces that exist for [basically every language under the sun](http://aws.amazon.com/code/Amazon-Mechanical-Turk).

