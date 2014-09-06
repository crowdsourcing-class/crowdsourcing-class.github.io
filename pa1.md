---
layout: default
img: python
caption: Hello world!
title: Homework 3 | Python Bootcamp
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before class on Wednesday, September 17.
</div>


Python Bootcamp <span class="text-muted">: Assignment 3</span> 
=============================================================
Enough talk, this week we will start writing some code. This assignment is designed to be a crash-course to get you up to speed on the level of Python you will need to know in order to do the remainder of the assignments. For those of you that already know Python, great. For those that do not, its easiest to learn by doing, so please start early so we can help you get on board so that you can focus on the crowdsourcing and machine learning, not the indenting and semicoloning. 

The majority of the assignment will focus on teaching you Python by walking you through building a simple machine learning classifier. The deliverables for this assignment will be :
1. Your script, bootcamp.py, which should contain your code for training and running your classifier on the provided data. 
2. Your answers to the questions [here](). 

You do not need to turn in anything for the first 3 sections, but you will need to read through them and do the exercises so that you can let us know ASAP if you are having trouble before we start on the real coding assignments.  

###1. The basics: variables and data structures

Python has your basic variable types: strings, ints, floats. Unlike Java and many other languages, variables are not typed. You simply declare a variable by assigning a value to it. Later, you can reassign a different type to that same variable and Python couldn't care less.

Open up the python interpreter and play with variable assignment and reassignment:

<pre><code>$ python
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 2
>>> x
2
>>> y = "hello world"
>>> y
'hello world'
>>> x = y 
>>> x
'hello world'
</code></pre>

This also means that you can mix variable types within a data structure. There is no need to specify that L is a list of ints or that M is a map from strings to floats; Python just has lists and maps.

Lists are declare with square brackets and indexed using square bracket notation. They can also be treated as stacks, if you are into that sort of thing. 

Create a list of ints. Then, in order to drive those Scala people insane, start appending strings to it. Play with indexing and slicing. In Python, you can use the colon notation to pull out slices of a list. E.g. lst[i:j] will give you a new list which includes the ith through the (j-1)th elements of lst.

<pre><code>>>> l = [1, 2, 3]
>>> for elem in l: print elem
... 
1
2
3
>>> l.append("i am a string. mwahahaha.")
>>> for elem in l: print elem
... 
1
2
3
i am a string. mwahahaha.
>>> l[2]
3
>>> l[1:3]
[2, 3]
>>> l += ['here is more stuff', 6, [2,3,4], 5*1367]
>>> print l
[1, 2, 3, 'i am a string. mwahahaha.', 'here is more stuff', 6, [2, 3, 4], 6835]
>>> l.pop()
6835
</code></pre>

Dictionaries (or maps or associative arrays) are probably the favorite data structure of Python. They are a simple key/value store, again without any restrictions on which data types are the keys or values. You can declare dictionaries with curly braces and associate or retrieve keys and values using square bracket notation.

<pre><code>>>> d = {"give me an A!" : "B", "give me a P!" : 7, "give me a Q!" : "no."}
>>> d["give me a P!"]
7
>>> d[14] = 12
>>> d
{'give me a Q!': 'no.', 'give me an A!': 'B', 14: 12, 'give me a P!': 7}
</code></pre>

As you can imagine, the lack of type-checking makes it very easy to write bad Python code. I would advise against doing so. But it is your call, some people like the thrill of nondeterministic runtime errors and such. Don't let me cramp your style.

###2. Control structures and functions

Python makes it easy to write bad code. But it makes it _very_ hard to write ugly code. So chalk one up for superficiality. Python use whitespace to denote control structures, like loops and if/else blocks, which makes the logic very intutive to read and means you don't have to worry about curly braces. By convention, you should use four spaces for each level of indentation. (I use tabs because I am lazy and like to save the key strokes. I was told over the summer that this is the mark of a novice, and no one of any merit uses tabs. I just hung my head in shame. So use spaces.)

<pre><code>
>>> print l
[1, 2, 3, 'here is more stuff', 6, [2, 3, 4]]
# Here is a for loop. The loop ends when you leave the indented block
>>> for elem in l:
...     print elem
... 
1
2
3
here is more stuff
6
[2, 3, 4]
# Here is a while loop
>>> i = 0
>>> while i < 5 : 
...     if i % 2 == 0 : 
...             print "even"
...     else : 
...             print "odd"
...     i += 1
... 
even
odd
even
odd
even
# Here is a function definition. Again, no types are required for your parameters, so commenting is SOOO important. So important.
"""
Returns the idx element of a list

lst - the list 
idx - the integer index of the element to return
"""
>>> def get_list_element(lst, idx) : 
...     return lst[idx]
... 
>>> get_list_element(l, 4)
6
</code></pre>

###3. File IO

###4. Text processing

###5. Machine learning in Python


Your code is due <b>Wednesday, September 17</b>. Please submit it via <code>turnin</code> from the eniac machines. 


