#Getting Started with IPython Notebooks

## Overview

IPython Notebooks are a platform for writing and running Python code to view output and produce visualizations instantaneously. It provides a number of feedback tools that will help you quickly create the best version of your code. 

## Installation

###1. First things first: Python!

We'll be using Python for the vast majority code we write in this course. If you've never written in Python, don't worry - we'll get you up to speed with the Python Bootcamp assignment. It's a high-level language with a great variety of applications, extremely readable, and will let us use IPython Notebooks. 

Python is likely already set up on your computer, but in order to confirm that, open up a command line (Terminal on OS X, Command Prompt on Windows, CLI on Linux) and type: 

`$ python `

You should receive some output with the version and some extra info, like below. If you don't, you need to download it. A guide to do so for a number of common operating systems is [here][python download]. 

[python download]:https://wiki.python.org/moin/BeginnersGuide/Download

```
Python 2.7.10 (default, Aug 22 2015, 20:33:39)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] 
on darwin
Type "help", "copyright", "credits" or "license" for more information. 
```


###2. Package Managers: Pip

Package managers are great tools to set up software and its dependencies on your computer. You'll use them a few times throughout the course, and familiarizing yourself with what they offer will give you a broader range of tools to use in your final project.

The exciting news is that the package manager we'll use to start, called pip, comes bundled with the Python installation that you just confirmed or completed. As long as the version that you saw when you typed `python` was above 2.7.9 or 3.4, you are guaranteed to have pip. To double-check, you can type `pip list` into your command line. If pip is installed, you'll see a long list of your packages print out. If pip isn't installed, you'll see an error message which tells you some variation of 'command not found.' If you see an error, you should first try [updating your version of Python][python download instructions] by downloading the most recent copy, and if that doesn't resolve it, [download pip directly][pip download link].

[python download instructions]:https://www.python.org/downloads/
[pip download link]:https://pip.pypa.io/en/stable/installing/

###3. Installing IPython Notebooks

You're in the home stretch of IPython Notebook set-up! Now you can return to your command line and run `$ pip install ipython[notebook]`.

You may need to give pip extra permissions to get IPython installed, so if you see any error messages or exceptions mentioning permissions or installation failing, run `$ sudo pip install ipython[notebook]`. When you are successful, you'll see some packages download and the command line wait for your next input. 

Type `$ ipython notebook` to launch a new browser tab that acts as a server for your notebooks. Here, on the dashboard, you can create new notebooks and modify existing notebooks and Python scripts. 

You're all set! 