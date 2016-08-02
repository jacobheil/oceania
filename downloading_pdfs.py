import glob, codecs, os, time, urllib2
from bs4 import BeautifulSoup

if not os.path.exists("oceania_pdfs"):
	os.makedirs("oceania_pdfs")

soup = BeautifulSoup(open("oceania.xml"), "xml")

for link in soup.find_all('src'):
    file = link.contents[0]
    file_link = file.strip()
    file_name = file_link[48:]

    print(file_name)

    response = urllib2.urlopen(file_link)
    file = open('oceania_pdfs/' + file_name, 'w')
    file.write(response.read())
    file.close()
    
    print("Completed")

	

	
 





