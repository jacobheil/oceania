import glob, codecs, os, time, urllib2,sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

#rep = {"condition1": "", "condition2": "text"} # define desired replacements here

'''
THIS script builds from "glomming_meta_test" in which I made one big XML file from the 

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
