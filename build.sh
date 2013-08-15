#!/bin/bash

./Markdown_1.0.1/Markdown.pl index.md | perl Markdown_1.0.1/wrap.pl > index.html
./Markdown_1.0.1/Markdown.pl syllabus.md | perl Markdown_1.0.1/wrap.pl > syllabus.html
./Markdown_1.0.1/Markdown.pl assignments.md | perl Markdown_1.0.1/wrap.pl > assignments.html
./Markdown_1.0.1/Markdown.pl resources.md | perl Markdown_1.0.1/wrap.pl > resources.html 
./Markdown_1.0.1/Markdown.pl pa1.md | perl Markdown_1.0.1/wrap.pl > pa1.html 
./Markdown_1.0.1/Markdown.pl pa2.md | perl Markdown_1.0.1/wrap.pl > pa2.html 
./Markdown_1.0.1/Markdown.pl pa3.md | perl Markdown_1.0.1/wrap.pl > pa3.html 
./Markdown_1.0.1/Markdown.pl pa4.md | perl Markdown_1.0.1/wrap.pl > pa4.html 
./Markdown_1.0.1/Markdown.pl pa5.md | perl Markdown_1.0.1/wrap.pl > pa5.html 
./Markdown_1.0.1/Markdown.pl wa1.md | perl Markdown_1.0.1/wrap.pl > wa1.html 
./Markdown_1.0.1/Markdown.pl wa2.md | perl Markdown_1.0.1/wrap.pl > wa2.html 
./Markdown_1.0.1/Markdown.pl wa3.md | perl Markdown_1.0.1/wrap.pl > wa3.html 
./Markdown_1.0.1/Markdown.pl wa4.md | perl Markdown_1.0.1/wrap.pl > wa4.html 
./Markdown_1.0.1/Markdown.pl midterm.md | perl Markdown_1.0.1/wrap.pl > midterm.html 
./Markdown_1.0.1/Markdown.pl progress.md | perl Markdown_1.0.1/wrap.pl > progress.html 
./Markdown_1.0.1/Markdown.pl final.md | perl Markdown_1.0.1/wrap.pl > final.html 
