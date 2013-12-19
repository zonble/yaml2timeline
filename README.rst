yaml2timeline
=============

- Weizhong Yang a.k.a zonble
- zonble {at} gmail {dot} com
- Friday, December 20, 2013

*yaml2timeline* was a in-house project management tool in KKBOX, an
online music streaming service provider in Asia. The tool is written
in Python programming language.

The tool does a simple job, it reads a YAML document which defines the
expected begin date and end date of each task, and render it into an
HTML file. The HTML file is made with an elegant timeline table, which
is created with Google Charts JavaScript API.

In KKBOX, we host the YAML file in a git repository so everyone can
simply edit it. And we display the HTML file on a TV. It helps us,
developers, to quickly have an overview about how many tasks that we
are working on, and to estimate if we have effert to start new
projects.

The best part is, we need not to explain how much work do we have to
our colleagues and boss anymore, but just say, "Hey! Watch the TV!"

Installation
------------

Launch terminal. Clone the project by calling

``git clone https://github.com/zonble/yaml2timeline.git``

Then run the following command

``[sudo] python setup.py install``

Usage
-----

Quite simple. Just run the following command

``yaml2timeline your_yaml_file output_html_file``

Done!

The YAML Document
-----------------

Your YAML document should look like

::

	<Project 1>:
	- {title: <Task 1>, begin: 2013-12-01, end: 2013-12-30}
	- {title: <Task 2>, begin: 2013-12-08, end: 2014-01-08}
	<Project 2>:
	- {title: <Task 1>, begin: 2013-12-01, end: 2013-12-30}
	- {title: <Task 2>, begin: 2013-12-08, end: 2014-01-08}

The rendered HTML will look like

..image:: https://raw.github.com/zonble/yaml2timeline/master/sample/sample.png

Enjoy it!
