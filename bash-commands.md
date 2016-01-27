---
layout: default
img: python
img_link: http://xkcd.com/353/
caption: Hello world!
title: Bash Cheat Sheet
active_tab: 
release_date: 
due_date: 
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
{% endif %}
<!-- End of check whether the assignment is up to date -->


Bash<span class="text-muted">: Greatest Hits</span> 
=============================================================

####Where am I??
{% highlight tcsh %}
$ ls # list all the files in this directory
$ ls some/directory # list all the files in some/directory
$ pwd # print the directory where you are currently working ("print working directory")
$ cd some/directory # go to some/directory ("change directory")
$ mkdir new_directory # create a new diretory called new_directory ("make directory")
$ rm file.txt # remove file.txt (be careful, it will be gone for good).
$ rm -r directory # remove directory and all the files within it (again, gone for good).
{% endhighlight %}

####What the $#@! are these files?
{% highlight tcsh %}
$ ls -lah file.txt #print the size of file.txt in bytes (also the date it was created)
$ wc -l file.txt #print the number of lines in file.txt
$ file file.txt #print the type of the file (e.g. is it a text file? compressed archive?)
$ head file.txt #print the first 10 lines of file.txt
$ head -NUM file.txt #print the first NUM lines of file.txt (e.g. head -3 prints first 3 lines)
$ tail -NUM file.txt #print the last NUM lines of file.txt (e.g. tail -3 prints last 3 lines)
$ cat file.txt #print the entire contents of file.txt
{% endhighlight %}

####Exploring and reorganizing file contents
{% highlight tcsh %}
$ sort file.txt # sort the lines in file.txt (by default, alphabetically and ascending)
$ sort -r file.txt # sort the lines in file.txt in reverse order
$ sort -nr file.txt # sort the lines in file.txt numerically and in reverse order
$ uniq file.txt # remove duplicate lines (only works if you use "sort" first)
$ uniq -c file.txt # print out unique lines and the number of times each one occurs
$ cut -f 1 file.txt # print the first column of the file.txt (assumes columns are tab-separated)
$ cut -f 1 -d ',' file.csv # print the first column of file.csv, split on comma instead of tab
$ grep "phrase" file.txt # print out lines in file.txt that contain the string "phrase"
$ grep -i "phrase" file.txt # same as above, but ignoring case
$ grep -v "phrase" file.txt # print out lines in file.txt that don't contain the string "phrase"
$ shuf file.txt # shuffle the lines in file.txt
{% endhighlight %}

####Gettin' fancy
Bash commands are connecting via "pipes", which means the input of one command is the output of the previous command. We use the | character to "pipe" one command's output into another. Below are some useful examples.
{% highlight tcsh %}
$ cat file.txt | sort | uniq | wc -l # how many unique lines are in this file
$ cat file.txt | sort | uniq -c | sort -nr # print out the unique lines in file.txt, with the most frequent line and its count at the top
$ cat file.txt | grep "phrase" | wc -l # how many lines in this file contain the phrase "phrase" 
$ cat file.txt | sort | uniq -c | sort -nr | head -100 | shuf | head -10 # take a random sample of 10 of the top 100 most frequent lines
{% endhighlight %}

