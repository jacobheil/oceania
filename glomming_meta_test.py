import glob, codecs, os, time, urllib2,sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

#rep = {"condition1": "", "condition2": "text"} # define desired replacements here

'''
Python script to extract xml data from the oceania files. I've saved them as .xml from .pdfs and am now trying to automate some way to get structure out of them. Not sure how this is going to go. Starting with this tutorial: 
		https://www.rdegges.com/2013/quickly-extract-xml-data-with-python/

'''
count = 0
#loc_count = 0
#ind_count = 0

if not os.path.exists("test_batch/test_xml_glom"):
    os.makedirs("test_batch/test_xml_glom")

for i in glob.glob("test_batch/test_xml/*.xml"): 
	
	#print i
	#count = count + 1
	#print count

	

	file_name = i.split('/')[-1][:-8]
	#count = count + 1
	
	with codecs.open(i,"r","utf-8") as doc:
		doc = doc.read()

		'''

		if 'Culture/location' or 'Culture/Location' in doc:
			count = count + 1

		else:
			print "not in " + file_name

		'''

		soup = BeautifulSoup(doc)

		newer_doc = soup.item_data.extract().prettify()

		with codecs.open("test_batch/test_xml_glom/test_xml_glom.xml",'a','utf-8') as out:
			out.write(unicode(newer_doc)+"\r\r")
		

print 'finished'
