#Writing a CSV from a HTML- scraping data

import csv
from urllib2 import urlopen
from bs4 import Beautifulsoup as Bet

html = urlopen("https://cricclubs.com/NTCA/teamSchedule.do?teamId=1636&clubId=343")
bsobj = Bet.Beautifulsoup(html, "lxml")
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
