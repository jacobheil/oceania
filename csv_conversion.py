import xml.etree.ElementTree as ET
import csv, sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
THIS script builds from "glomming_meta_test" in which I made one big XML file from the indiv. files in test_xml dir. I want to convert "test_xml_glom.xml" to a CSV file to use as the basis for an upload to Omeka. Starting here: http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-xml-to-csv-using-python/

'''
count = 0
#loc_count = 0
#ind_count = 0

tree = ET.parse("test_batch/test_xml_glom/test_xml_glom.xml")
root = tree.getroot()

# open a file for writing

item_data = open('test_batch/test_xml_glom/item_data.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(item_data)
header = []
# Creating an empty array to store the header information below. 

count = 0
for item in root.findall('item_data'):
	item_list = []
	if count == 0:
		imagedata = item.find('imagedata').tag
		header.append(imagedata)
		obj_type = item.find('obj_type').tag
		header.append(obj_type)
		indig_name = item.find('indig_name').tag
		header.append(indig_name)
		cult_loc = item.find('cult_loc').tag
		header.append(cult_loc)
		date = item.find('date').tag
		header.append(date)
		materials = item.find('materials').tag
		header.append(materials)
		dimensions = item.find('dimensions').tag
		header.append(dimensions)
		inst_access = item.find('inst_access').tag
		header.append(inst_access)
		source = item.find('source').tag
		header.append(source)
		csvwriter.writerow(header)
		count = count + 1

	imagedata = item.find('imagedata').text
	item_list.append(imagedata)
	obj_type = item.find('obj_type').text
	item_list.append(obj_type)
	indig_name = item.find('indig_name').text
	item_list.append(indig_name)
	cult_loc = item.find('cult_loc').text
	item_list.append(cult_loc)
	date = item.find('date').text
	item_list.append(date)
	materials = item.find('materials').text
	item_list.append(materials)
	dimensions = item.find('dimensions').text
	item_list.append(dimensions)
	inst_access = item.find('inst_access').text
	item_list.append(inst_access)
	source = item.find('source').text
	item_list.append(source)
	csvwriter.writerow(item_list)
item_data.close()

print 'finished'