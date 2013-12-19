===============
 yaml2timeline
===============

Weizhong Yang
Friday, December 20, 2013

*yaml2timeline* was a in-house tool for project management in KKBOX,
an online music streaming service in Asia.

The tool does a simple job, it reads a YAML document which defines the
expected begin date and end date of each task, and render it into an
HTML file.

Installation
------------

Launch terminal. Clone the project by calling

::
	``git clone https://github.com/zonble/yaml2timeline.git``

Then run the following command

::
	``[sudo] python setup.py install``

Usage
-----

Quite simple. Just run the following command

::
   ``yaml2timeline your_yaml_file output_html_file``

Done!

The YAML Document
-----------------

Your YAML document should look like

::
	<Project Name>:
	- {title: <Task 1>, begin: 2013-12-01, end: 2013-12-30}
	- {title: <Task 2>, begin: 2013-12-08, end: 2014-01-08}
