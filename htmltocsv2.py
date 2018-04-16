#Writing a CSV from a HTML- scraping data

import csv
import urllib
from bs4 import Beautifulsoup

html = urlopen("https://cricclubs.com/NTCA/teamSchedule.do?teamId=1636&clubId=343")
bsobj = Beautifulsoup(html, "lxml")
table = bsobj.findall("table", {"class":"sortable table"})[0]
rows = table.findall("tr")
csvFile = open("ntca.csv", 'wt', newline='')
writer = csv.writer(csvFile)
try:
    for row in rows:
        
        csvRow = []
        for cell in row.findall(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
        csvFile.close()
