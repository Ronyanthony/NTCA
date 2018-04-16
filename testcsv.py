'''
import csv

csvFile = open('test.csv', 'w+', newline='')
#print (int(csvFile.size))
#print (csvFile)
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number' , 'number plus 2' , 'number times 2'))
    for i in range (5):
        writer.writerow((i, i+4, i*5))
finally:
        csvFile.close()
'''

x = [1, 2, 3, 4, 5] 
#print (x)
row = 5
col = 5 
for row in range(len(x)):
    #print ("test")
    sub = []
    for col in range(len(x)):
        sub.append(1)
        break
    print(sub)
