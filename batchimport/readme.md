#Django Batch Import
This is a port of the app at http://code.google.com/p/django-batchimport/ but updated to work with Django 1.5. I have also made a few changes to the URL's etc and secured it so you had to have Admin priveleges to use it.

Batch import will allow you to quickly import large amounts of data into your Django database from Excel files (.xls) It assumes the first row of your spreadsheet is made up of headers for the rows and matches them to the names of your model. It has worked really well for me and a huge hat tip to the original author!

##Installation
The python package XLRD is required. You should be able to install it with

	pip install xlrd

on your server. You can use any spreadsheet as long as you save it as an Excel .xls file first.

Simply place this module anywhere on your projects' python path and then edit settings.py and add it to your installed modules.

	INSTALLED_APPS = (
	...
	'batchimport',
	)
	
Then in your urls.py add something like:

	url(r'^batchimport/', include('batchimport.urls')),
	
After a restart you should be able to go to yourproject.com/batchimport/ and begin the import process.