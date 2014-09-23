---
layout: default
img: capitalist-greed
caption: Exploit the masses!
title: Homework 5 | Become a Requester
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, October 1st.</div>


Become a Requester<span class="text-muted">: Assignment 5</span> 
=============================================================

Last week, you built a classifier to predict whether or not an article was about gun violence. You were able to estimate how well your classifier did by using [cross validation](), and you probably ended up with some accuracies that were pretty damn near perfect. But a very good question to ask is, why train a model to label articles that already have labels?  The real point of machine learning is not to predict things that you already have answers to, but to try to predict new things. In this case, we want to see if our classifier can look at new articles that no one has labeled, and predict whether or not they are about guns. 

Predicting on data "in the wild" is much harder than predicting on the clean training data. Before, we cleaned your training data using the [Alchemy API]()'s state of the art processing, which gave us clean articles like this:

<i>"After a 14-year-old was gunned down Thursday night it appears Chicago went 42 hours without a shooting, but that streak came to an end Saturday afternoon when two people were shot near Ogden Park. Rarely is there a 42-hour period in Chicago without a shooting, particularly at the start of a warm holiday weekend. Some activists are crediting Chicago Police and community efforts with starting to pay off. "Maybe it's beginning to change, maybe this thing's going to turn around," said Father Michael Pfleger. Saturday evening mass at St. Sabina Church Saturday night is a time to celebrate a victory over violence, even if for less than a 48-hour period."</i>

Now, your data has been scraped from the web, with cheaper, faster, hand-written-er (and drastically worse, why lie?) processing, so you might get articles like this:

<i>"Boy, 3, among 13 injured in Chicago park shooting .zone Boy, 3, among 13 injured in Chicago park shooting #adgSocialTools #adgSocialTools div.social_header #adgSocialTools div.social_main #adgSocialTools div.social_main img, #adgSocialTools div.social_footer img #adgSocialTools div.social_footer #adgSocialTools div.social_footer img.btn_sm_right #adgSocialTools img.btn_lg CHICAGO Thirteen people have been shot at a park on Chicago's southwest side, including a 3-year-old boy who was in critical condition, in what authorities say was likely a gang-related shooting."</i>

You can probably imagine that that 99% accuracy on cross validation may have been misleading. So this week we will get a real estimate of how well your classifier can do by taking the articles that your classifier thinks are gun-related, and asking workers on Crowdflower whether they agree or disagree with these predictions.


This assignment has two parts:

1. You will need to run your classifier from last week on [these 1.4 million unlabeled articles](), and pull out the articles that it thinks are gun-related.
2. You will create a task on [Crowdflower]() in which workers will label a sample of the articles, and recalculate your classifier's accuracy.




