---
layout: default
img: tar
caption: Life skills
title: XPath
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


XPath<span class="text-muted">: Enough to get by</span> 
=============================================================

XPath is a syntax for selecting nodes out of xml-formatted documents. You can look at the tutorials [here](http://www.w3schools.com/xsl/xpath_examples.asp) and [here](http://www.w3schools.com/xsl/xpath_syntax.asp). Below are some basic examples that should suffice for our assignments. Shown in the boxes are code snippets, followed by the output that results from running them. You can [download the code and example xml file](http://crowdsourcing-class.org/assignments/downloads/xpath-examples.tgz) for these examples if you want to change and test them yourself.

* Assume you have the below xml document, which contains inventory for a bookstore.

<pre></code>
&lt;bookstore location="Philadelphia"&gt;
  &lt;book category="COOKING"&gt;
    &lt;title lang="en"&gt;Everyday Italian&lt;/title&gt;
    &lt;author&gt;Giada De Laurentiis&lt;/author&gt;
    &lt;year&gt;2005&lt;/year&gt;
    &lt;price&gt;30.00&lt;/price&gt;
  &lt;/book&gt;
  &lt;book category="CHILDREN"&gt;
    &lt;title lang="es"&gt;Harry Potter&lt;/title&gt;
    &lt;author&gt;J K. Rowling&lt;/author&gt;
    &lt;year&gt;2005&lt;/year&gt;
    &lt;price&gt;29.99&lt;/price&gt;
  &lt;/book&gt;
  &lt;dvd category="COMEDY"&gt;
    &lt;title lang="en"&gt;Legally Blonde&lt;/title&gt;
    &lt;year&gt;2001&lt;/year&gt;
    &lt;price&gt;9.95&lt;/price&gt;
  &lt;/dvd&gt;
&lt;/bookstore&gt;
</code></pre>

* We can read in the xml file using lxml

<pre><code>&gt;&gt; import lxml.etree
&gt;&gt; doc = lxml.etree.parse(open('example.xml'))</code></pre>
	
* Single slashes (/) select from the root node (here, the root is whatever invisible node exists above "bookstore"). So we access bookstore and its attributes using single slashes.

<pre><code>&gt;&gt; print "Bookstore locations"
&gt;&gt; for bookstore in doc.xpath('/bookstore'):
&gt;&gt;   print bookstore.get('location')
Bookstore locations
Philadelphia
</code></pre>

* We **cannot** access "book" nodes using single slashes, since they are not direct children of the root. The below code produces no output.

<pre><code>&gt;&gt; print "Book categories"
&gt;&gt; for book in doc.xpath('/book'):
&gt;&gt;   print book.get('category')
Book categories
</code></pre>

* We can use the double slash (//) to select nodes below from the current node, appearing anywhere in the tree (not just direct children of the current node). This way, we can access "book" like we failed to do in the above snippet. Or to select all the dvds.

<pre><code>&gt;&gt; print "Book categories"
&gt;&gt; for book in doc.xpath('//book'):
&gt;&gt;   print book.get('category')
Book categories
COOKING
CHILDREN

&gt;&gt; for book in doc.xpath('//dvd'):
&gt;&gt;   print book.get('category')
DVD categories
COMEDY
</code></pre>

* If you use the double slash to select titles, you will get all the "title" nodes, regardless of whether they are book or dvd titles.

<pre><code>&gt;&gt; print "All titles"
&gt;&gt; for title in doc.xpath('//title'):
&gt;&gt;   print '%s available in language %s'%(title.text, title.get('lang'))
All titles
Everyday Italian available in language en
Harry Potter available in language es
Legally Blonde available in language en
</code></pre>

* You can chain together both types of slahes, to great longer paths. E.g. you can use the code below to only select title nodes that appear as children of dvd nodes.

<pre><code>&gt;&gt; print "Only DVD titles"
&gt;&gt; for title in doc.xpath('//dvd//title'):
&gt;&gt;   print '%s available in language %s'%(title.text, title.get('lang'))
Only DVD titles
Legally Blonde available in language en
</code></pre>
