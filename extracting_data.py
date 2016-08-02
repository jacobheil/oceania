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

#if not os.path.exists("oceania_pdfs/_ocr_output_parsed"):
#    os.makedirs("oceania_pdfs/_ocr_output_parsed")

for i in glob.glob("oceania_pdfs/_ocr_output_xml/*.xml"): 
	
	#print i
	#count = count + 1

	file_name = i.split('/')[-1][:-4]
	#count = count + 1
	
	with codecs.open(i,"r","utf-8") as doc:
		doc = doc.read()

		

		if 'Indigenous name' in doc:
			count = count + 1

		else:
			print "not in " + file_name

		'''

		new_doc = doc.replace('Object Type', \r'<object type>').replace('Object type', '<"object_type>').replace('Culture/location', '<cult_loc>').replace('Culture/Location', '<cult_loc>').replace('Culture/ location', '<cult_loc>').replace('Indigenous name', '<indig_name>').replace('Bibliography', '<bibl>').replace('Date', '<date>').replace

		with codecs.open("oceania_pdfs/_ocr_output_parsed/" + file_name + '_parsed.xml','w','utf-8') as out:
			out.write(new_doc)
		'''

print count
