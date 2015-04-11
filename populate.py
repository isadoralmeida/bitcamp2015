from os
from xml.dom import minidom

xmldoc = minidom.parse(argv[0])
item = xmldoc.getElementsByTagName('ReportedCrimes')
for i in item:
	item2 = xmldoc.getElementsByTagName('ReportedCrime')
	