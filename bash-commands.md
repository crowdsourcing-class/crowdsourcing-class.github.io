---
layout: default
img: tar
caption: Life skills
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

#### Where am I??
{% highlight tcsh %}
$ ls # list all the files in this directory
$ ls some/directory # list all the files in some/directory
$ pwd # print the directory where you are currently working ("print working directory")
$ cd some/directory # go to some/directory ("change directory")
$ cd ~/ # take me home ("change directories to the user's home directory")
$ mkdir new_directory # create a new diretory called new_directory ("make directory")
$ rm file.txt # remove file.txt (be careful, it will be gone for good).
$ rm -r directory # remove directory and all the files within it (again, gone for good).
{% endhighlight %}

#### What the $#@! are these files?
{% highlight tcsh %}
$ ls -lah file.txt #print the size of file.txt in bytes (also the date it was created)
$ wc -l file.txt #print the number of lines in file.txt
$ file file.txt #print the type of the file (e.g. is it a text file? compressed archive?)
$ head file.txt #print the first 10 lines of file.txt
$ head -NUM file.txt #print the first NUM lines of file.txt (e.g. head -3 prints first 3 lines)
$ tail -NUM file.txt #print the last NUM lines of file.txt (e.g. tail -3 prints last 3 lines)
$ cat file.txt #print the entire contents of file.txt
$ tar -xzvf file.tar.gz #unzip a tar archived file
$ tar -czvf files.tar.gz files/ #create a tar archived file containing the contents of the directory files/
{% endhighlight %}

#### Exploring and reorganizing file contents
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

#### Gettin' fancy
Bash commands are connecting via "pipes", which means the input of one command is the output of the previous command. We use the | character to "pipe" one command's output into another. Below are some useful examples.
{% highlight tcsh %}
$ cat file.txt | sort | uniq | wc -l # how many unique lines are in this file
$ cat file.txt | sort | uniq -c | sort -nr # print out the unique lines in file.txt, with the most frequent line and its count at the top
$ cat file.txt | grep "phrase" | wc -l # how many lines in this file contain the phrase "phrase" 
$ cat file.txt | sort | uniq -c | sort -nr | head -100 | shuf | head -10 # take a random sample of 10 of the top 100 most frequent lines
{% endhighlight %}
Bash can also write to files! This makes a life a lot easier than dragging your cursor, copying large chunks of text from the terminal window. File Output Redirection can be done using the <code> > </code> or <code> >> </code> operators. 
{% highlight tcsh %}
$ grep "Hello" file.txt > output.txt # Stores every line containing "Hello" in file.txt in a new file output.txt
$ cat file.txt | sort | uniq -c | sort -nr > output.txt # stores the unique lines of file.txt, with the most frequent line and its count at the top, in output.txt. Overwrites the old contents of output.txt (Careful!)
$ cat output.txt | wc -l >> output.txt # Appends the line count of output.txt to the end of output.txt
{% endhighlight %}

#### Downloading Files
To download the contents of any URL (whether it be a file, HTML page or even a picture), there's a very useful command on Mac and Linux.
{% highlight tcsh %}
$ wget http://www.crowdsourcing-class.org/assignment1.html # Downloads the contents of the URL as th file 'assignment1.html' to the current directory (used in Linux)
{% endhighlight %}
{% highlight tcsh %}
$ curl -O http://www.crowdsourcing-class.org/assignment1.html # Downloads the contents of the URL as th file 'assignment1.html' to the current directory (used in Mac)
{% endhighlight %}

#### Uploading Files and Directories
To turn in your HWs, you need to log into the remote SEAS server (ENIAC) and use the <code>turnin</code> tool. There are some commands below which show how to transfer your HW files from your local computer to another machine / server over SSH. The <code>:~/</code> at the end is required always. For directories, the <code>-r</code> flag is required. For Penn students, the username is your Pennkey.
{% highlight tcsh %}
$ scp your_file_name username@serveraddress:~/ # This copies the file "your_file_name" to the remote server. 
$ scp answers.txt johndoe@eniac.seas.upenn.edu:~/ # This copies answers.txt to ENIAC. 
$ scp -r your_dir username@serveraddress:~/ # This copies the entire directory "your_dir" to the remote server.
$ scp -r NETS213_HW johndoe@eniac.seas.upenn.edu:~/ # This copies the NETS213_HW directory to the remote server.
{% endhighlight %}

