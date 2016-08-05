# Script for closing tags. 

import glob, codecs, os, time, urllib2,sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

count = 0

if not os.path.exists("oceania_pdfs/_ocr_output_structured"):
    os.makedirs("oceania_pdfs/_ocr_output_structured")

for i in glob.glob("oceania_pdfs/_ocr_output_parsed/*.xml"): 
	
	#print i
	#count = count + 1

	file_name = i.split('/')[-1][:-10]
	
	#count = count + 1
	
	with codecs.open(i,"r","utf-8") as doc:
		doc = doc.read()

		
		'''
		# Open this partition (and uncomment partition above final print statements) to run count tests for terms in the doc.

		if '</inst_access></dimensions></materials></date></cult_loc></indig_name></obj_type></inst_access></dimensions></materials></date></cult_loc></indig_name></obj_type>' in doc:
			count = count + 1

		else:
			print "not in " + file_name

		'''

		new_doc = doc.replace('</inst_access>', '').replace('</dimensions>', '').replace('</materials>', '').replace('</date>', '').replace('</indig_name>', '').replace('</cult_loc>', '').replace('</obj_type>', '')

		#soup = BeautifulSoup(new_doc)

		#newer_doc = soup.part.extract()
			

		with codecs.open("oceania_pdfs/_ocr_output_structured/" + file_name + 'structured.xml','w','utf-8') as out:
			out.write(unicode(newer_doc))
		# '''

print count
print 'finished'
