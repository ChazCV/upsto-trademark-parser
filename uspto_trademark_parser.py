import glob
import sqlite3

import lxml.etree as ET

#Connect to the SQLite database and create a table to store the parsed data.
conn = sqlite3.connect('trademark_classes_1-5.db')
c = conn.cursor()
c.execute('''CREATE TABLE TRADEMARKS(MARK TEXT, ADDRESS TEXT, INT CODE TEXT,
			 OWNER TEXT, AKA TEXT, SERIAL TEXT, REGISTRATION TEXT,
			 STATUS CODE TEXT, FILING DATE TEXT)''')

#Directory for files to be parsed.
for file in glob.glob('uspto/*'): 

	#Each 'case-file' node begins a single trademark application.
    tree = ET.iterparse(f, tag="case-file")
    for event, child in tree:
      	
		#Parse trademarks that have a written and non-empty identification.	
        mark = child.xpath("case-file-header/mark-identification/text()")
	    if mark:
		   
		    #Include desired data for extraction.
			status_code = child.xpath(
				"case-file-header/status-code/text()")
			address = child.xpath(
				"correspondent/address-5/text()")    
			mark = child.xpath(
				"case-file-header/mark-identification/text()")
			serial_number = child.xpath("serial_numberal-number/text()")
			registration_number = child.xpath(
				"registration_numberstration-number/text()")
			filing_date = child.xpath("case-file-header/filing-date/text()")
			international_class = child.xpath(
				"classifications/classification/international-code/text()")
			owner = child.xpath(
				"case-file-owners/case-file-owner/party-name/text()")
			alternate_owner = child.xpath(
				"case-file-owners/case-file-owner/dba-aka-text/text()")                                                   
			
			#Format and write rows to the SQL database.
			row = [(str(mark), str(address), str(international_class),
					str(owner), str(alternate_owner), str(serial_number), 
					str(registration_number), str(status_code),
					str(filing_date))]				
			c.executemany("INSERT INTO TRADEMARKS VALUES(?,?,?,?,?,?,?,?,?)",
						  row)
			
			#Clear nodes when they are no longer needed.
			child.clear()
        else:
            child.clear()
    else:
        child.clear()
#Save changes made to the database and exit when finished.    
conn.commit()
conn.close()