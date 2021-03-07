---
layout: default
img: xkcd-computer-vision
caption: In the 60s, Marvin Minsky assigned a couple of undergrads to spend the summer programming a computer to use a camera to identify objects in a scene. He figured they'd have the problem solved by the end of the summer. Half a century later, we're still working on it
title: Homework 5 "Training a classifier"
active_tab: homework
release_date: 2020-03-07
due_date: 2021-03-13T23:59:00EST
submission_link: https://www.gradescope.com/courses/233619/
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->


<div class="alert alert-info">
This assignment is before {{ page.due_date | date: "%I:%M%p" }}  due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>


Training Classifiers<span class="text-muted"> : Assignment 5</span> 
=============================================================

## Part 1: Training an Image Classifier

This week we will learn how to use the annotations that you collected as a Requester on Amazon Mechanical Turk to train image classifiers. We will be using [fastai](https://docs.fast.ai/), which is a wrapper around PyTorch that helps people get quickly started with deep learning.   Deep learning uses multi-layer neural networks. Applications of deep learning can be found all around you, including speech recognition, autonomous driving, and board games.

The creators of Fast AI have created a bunch of very good tutorials that are a hands-on practical introduction to deep learning for coders.  You will watch [Lesson 1](https://course.fast.ai/videos/?lesson=1) for an introduction to deep learning, and follow along with their [Python notebook](https://colab.research.google.com/github/fastai/fastbook/blob/master/01_intro.ipynb). 

We'll then adapt the Fast AI example so that we use deep learning to classify wedding photos in [our Colab notebook for image classification](https://colab.research.google.com/github/crowdsourcing-class/crowdsourcing-class.github.io/blob/master/assignments/hw5/Train_a_Classifier_Weddings_Dataset_STUDENT.ipynb).  You will write code in several places in our notebook.  You'll load in the aggregated results that we all collected from Amazon Mechanical Turk to get labeled training data.  You'll aggregate the Turkers' labels with voting to determine whether an image represents a wedding or not.  We will use these labels to train the classifier.

We'll also try training different versions of the wedding photo classifier to see the effects of representation in data collections.  The first version of our classifer will be trained only on Western weddings, and the next will be expanded to include Indian weddings as well.  

## Part 2: Training a Text Classifier

Text classification is one of the tasks that is addressed in natural language processing (NLP).  Like with computer vision, NLP uses deep learning.  A particular kind of deep learning model that is used in NLP is called the transformer.  If you're interested in learning  about transformers in this [blog post](http://jalammar.github.io/illustrated-transformer/).  We'll be using an implementation of transformers from an open source package called Hugging Face.  

For this assignment, we'll look at wallk through a text classification task called *intent detection*.  When you talk to your Amazon Alexa, it needs to figure out what you're trying to do.  If you say "add five mintues to my chicken timer", what are you trying to do? Are you trying to play music?  Do you want to check the weather?  Are you setting a timer?  Are you trying to get a recipe to cook something?  Depending on what it thinks your intent is, it routes your message to a specialized module to handle your request.


<div class="panel panel-info">
<div class="panel-heading" markdown="1">
#### Instructions
</div>
<div class="panel-body" markdown="1">
1. [Watch Lesson 1 on image classification](https://course.fast.ai/videos/?lesson=1), following along in [your own copy of the accompanying Python notebook](https://colab.research.google.com/github/fastai/fastbook/blob/master/01_intro.ipynb) - it's fun, and you'll learn more by runnning code!
2. Make a copy of [this Google Colab notebook for image clasification](https://colab.research.google.com/github/crowdsourcing-class/crowdsourcing-class.github.io/blob/master/assignments/hw5/Train_a_Classifier_Weddings_Dataset_STUDENT.ipynb), and then work through the assignment.  The parts that you have to code are marked with
```python
##### START CODE HERE
##### END CODE HERE 
```
3. Make a copy of [this Google Colab notebook for text classification](https://colab.research.google.com/github/crowdsourcing-class/crowdsourcing-class.github.io/blob/master/assignments/hw5/Assignment_5_–_Transformers.ipynb), and then work through the assignment.  The parts that you have to code are marked with
```python
## TO DO:
... 
```
4. [Answer the following Homework 5 questions on Gradescope]({{page.submission_link}}).  There you will submit links to your Colab notebooks with all the outputs shown.
</div>
</div>


<div class="panel panel-primary" id="questions">
<div class="panel-heading" markdown="1">
#### Questions
</div>
<div class="panel-body" markdown="1">

Below are the questions that you will be asked to answer about this assignment. Please turn in your answers for [Homework 5 on Gradescope]({{page.submission_link}}).

1. What is the link to your Colab notebook?
2. What is the difference between classification and regression?
3. What is a validation set? What is a test set? Why do we need them?
4. What does it mean to “normalize” images?
5. What is “overfitting”, and how do you try to avoid it?
6. Interpret the accuracy plot of the transformer model. Is the accuracy dependent on the train_size parameter? Would you say that the model is performing well overall? Why or why not?
</div>
</div>
