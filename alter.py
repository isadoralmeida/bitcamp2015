import sys
import xml.etree.ElementTree as ET
import re
import MySQLdb

tree = ET.parse(sys.argv[1])
root = tree.getroot()
db = MySQLdb.connect(host="localhost",user="root",passwd="bitcamp2015",db="bitcamp1")
cur = db.cursor()

for child in root:
	obj = {}
	for items in child:
		obj[items.tag[len("{http://dc.gov/dcstat/types/1.0/}"):]] = items.text
		if(obj[items.tag[len("{http://dc.gov/dcstat/types/1.0/}"):]] is None):
			obj[items.tag[len("{http://dc.gov/dcstat/types/1.0/}"):]] = "null"
	#query1 = ("Insert into CrimeLocation values (" + obj["neighborhoodcluster"] + "," + '"' + obj["district"] + '"' + "," + '"' + obj["block_group"] + '"' + "," + '"' + obj["ward"] + '"' + "," + '"' + obj["anc"] + '"' + "," + obj["blockxcoord"] + "," + obj["blockycoord"] + ");")
	#query2 = ("Insert into ReportedCrimes values (" + obj["ccn"] + "," + '"' + obj["reportdatetime"] + '"' + "," + '"' + obj["shift"] + '"' + "," + '"' + obj["offense"] + '"' + "," + '"' + obj["method"] + '"' + "," +  '"' + obj["lastmodifieddate"] + '"' + "," + '"' + obj["blocksiteaddress"] + '"' + "," + '"' + obj["businessimprovementdistrict"] + '"' + "," + obj["blockxcoord"] + "," + obj["blockycoord"] + "," + obj["psa"] + "," + obj["census_tract"] + "," + '"' + obj["voting_precinct"] + '"' + "," + '"' + obj["start_date"] + '"' + "," + '"' + obj["end_date"] + '"' + ");")
	time_division = obj["reportdatetime"].split("T")
	day_time = time_division[0].split("-")
	time_hour = time_division[1].split("-")
	query3 = ('Update ReportedCrimes SET year=' + day_time[0] + ',month=' + day_time[1] + ',day=' + day_time[2] + ',time="' + time_hour[0] + '",time_zone="' + time_hour[1] +'" Where cnn=' + obj["cnn"]+';')
	#print obj["reportdatetime"] + " - " + query3
	#print query2
	try:
		cur.execute(query3)
		#cur.execute(query2)
		db.commit()
	except:
		db.rollback()

db.close()