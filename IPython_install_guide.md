---
layout: default
title: IPython Notebook Install Guide
active_tab: resources
---

#Getting Started with IPython Notebooks

## Overview

IPython Notebooks are a platform for writing and running Python code to view output and produce visualizations instantaneously. It provides a number of feedback tools that will help you quickly create the best version of your code. 

## Installation

###1. First things first: Python!

We'll be using Python for the vast majority code we write in this course. If you've never written in Python, don't worry - we'll get you up to speed with the Python Bootcamp assignment. It's a high-level language with a great variety of applications, extremely readable, and will let us use IPython Notebooks. 

Python is likely already set up on your computer, but in order to confirm that, open up a command line (Terminal on OS X, Command Prompt on Windows, CLI on Linux) and run after the prompt (`$`): 

`python --version`

You should receive some output with the version, like below. 

```
Python 2.7.10
```

Either 2.7 or 3.4+ is fine -- different versions have different library support, but both will work for our purposes. If you don't have Python, you need to download it. A guide to do so for a number of common operating systems is [here][python download]. 

[python download]:https://wiki.python.org/moin/BeginnersGuide/Download



###2. Package Managers: Pip

Package managers are great tools to set up software and its dependencies on your computer. You'll use them a few times throughout the course, and familiarizing yourself with what they offer will give you a broader range of tools to use in your final project.

The exciting news is that the package manager we'll use to start, called pip, comes bundled with the Python installation that you just confirmed or completed. As long as the version that you saw when you typed `python` was above 2.7.9 or 3.4, you are guaranteed to have pip. To double-check, you can type `pip --version` into your command line. If it's installed, you'll see your version and possibly where you got it. If pip isn't installed, you'll see an error message which tells you some variation of 'command not found.' If you see an error, you should first try [updating your version of Python][python download instructions] by downloading the most recent copy, and if that doesn't resolve it, [download pip directly][pip download link].

[python download instructions]:https://www.python.org/downloads/
[pip download link]:https://pip.pypa.io/en/stable/installing/

###3. Installing IPython Notebooks

You're in the home stretch of IPython Notebook set-up! Now you can return to your command line and run `$ pip install ipython[notebook]`.

#####Debugging Tips: 

* If you are running OS X verion 10.11 "El Capitan" then the operating system may be blocking you from installing anything into `/System/Library/Frameworks/Python.framework/Versions/2.7/shar` even with the sudo command.  Instead try running `pip install --user ipython[notebook]`

* You may need to give pip extra permissions to get IPython installed, so if you see any error messages or exceptions mentioning permissions or installation failing, run `$ sudo pip install ipython[notebook]`. When you are successful, you'll see some packages download and the command line wait for your next input. 

* At this point, some users have seen an error: "IPython 4.0.1 does not provide the extra 'notebook.'" If you see this, you can resolve it by running:

`$ pip install -Iv ipython[notebook]==3.2.0` instead of `$ pip install ipython[notebook]`

* If you're using Anaconda, some included libraries have conflicts that prevent the kernel from running after you attempt to start a notebook. If you're using Anaconda, be sure to run: 

`conda install ipython-notebook`

* [Post to Piazza if you encounter any problems](https://piazza.com/class/ijblb017ius5zp?cid=39) not listed here - it's likely that others in the class will run into the same thing. 

#####Finally:

Type `ipython notebook` to launch a new browser tab that acts as a server for your notebooks. Here, on the dashboard, you can create new notebooks and modify existing notebooks and Python scripts. 

You're all set! 