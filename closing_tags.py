# Script for closing tags. 

import glob, codecs, os, time, urllib2,sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

if not os.path.exists("oceania_pdfs/_oceania_metadata"):
    os.makedirs("oceania_pdfs/_oceania_metadata")

for i in glob.glob("oceania_pdfs/_ocr_output_structured/*.xml"): 
	
	#print i
	#count = count + 1

	file_name = i.split('/')[-1][:-14]
	
	#count = count + 1
	
	with codecs.open(i,"r","utf-8") as doc:
		doc = doc.read()

		
		'''
		# Open this partition (and uncomment partition above final print statements) to run count tests for terms in the doc.

		if '<imagedata src="images/' in doc:
			count = count + 1

		else:
			print "not in " + file_name

		'''

		#new_doc = doc.replace('<part>\r', '<part>\r<metadata>\r')

		soup = BeautifulSoup(doc)

		newer_doc = soup.metadata.extract()
			

		with codecs.open("oceania_pdfs/_oceania_metadata/" + file_name + 'meta.xml','w','utf-8') as out:
			out.write(unicode(newer_doc))

		count = count + 1

		 # '''

print count
print 'finished'
