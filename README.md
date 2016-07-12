# upsto_trademark_parser

Script to parse a directory containing United States Patents and Trademark Office(USPTO) trademark application files,
and save the extracted data to a SQLite database. The files are in XML format and can be found here:
http://patents.reedtech.com/tmappxml.php#1884-2015 

Status codes represent the legal standing of a trademark from the time of a given mark's initial application, and as
the mark undergoes any changes. While the USPTO's Trademark Electronic Search System (TESS) offers a Live/Dead 
Boolean status for a returned trademark search, this data is not included in the XML files. However, it may be 
possible to determine a trademark's Live/Dead status through further analysis of the status codes themselves. 
An official list of status codes can be found here:
http://www.uspto.gov/web/offices/com/sol/og/con/files/cons181.htm
