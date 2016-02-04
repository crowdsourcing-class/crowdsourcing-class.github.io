---
layout: default
img: linux
caption: Windows Woes
title: VM Installation Instructions
active_tab: 
release_date: 
due_date: 
---

VM Installation Instructions
=============================================================

So a number of resources associated with this class rely on Python and other utilities which are woefully difficult to get working on Windows. In order to make your life a little easier, and give you the pleasure of saying you've dabbled with Linux, we're giving you the power to run Linux for this course!

#### Setup Virtual Machine Environment.

To start, install [VirtualBox](https://www.virtualbox.org/wiki/Downloads). You'd want to get the [VirtualBox 5.0.14 for Windows hosts](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-Win.exe). The one for Mac OSX can be downloaded here : [VirtualBox 5.0.14 for OS X hosts](http://download.virtualbox.org/virtualbox/5.0.14/VirtualBox-5.0.14-105127-OSX.dmg).

#### Install VirtualBox

Double click on the <code>.exe</code> or <code>.dmg</code> file you just downloaded and go through the installation process. It should be pretty easy and self explanatory.

#### Downloading the Disk Image

We've prepped a Ubuntu Disk Image for you with all the libraries required for the course pre-installed. In case you have to install other libraries, it should be pretty simple as we're using a standard Linux distribution. Download the Disk Image [here](https://s3.amazonaws.com/nets213vm/NETS-213.vdi).

#### Getting started with VirtualBox

* Open up VirtualBox and select "New"
* In the box that opens:
	* Name : "NETS 213"
	* Type : Linux
	* Version : Ubuntu (64-bit)
	* Memory : Set it to 2 GB (2048 MB)
	* Select the "Use an existing virtual hard disk file"
	* Choose the "NETS-213.vdi" file
	* Create
* Once created, double click on the "NETS 213" VM created.
* The login password is "nets213". This will also be the password you use with the <code>sudo</code> command.

And you're all set! No more worrying about compatibility or <code>$PATH</code> variable issues!


