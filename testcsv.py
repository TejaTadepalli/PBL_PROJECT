import csv

file=open('songs_list (3).csv')
type(file)

csvreader=csv.reader(file)

header=[]
header=next(csvreader)

print(header)

#rows=[]
#for row in csvreader:
#    rows.append(row)
#print(rows)

#for i in header:
#    if(header[i]=='Bell'):
#        if()
