import pandas as pd

import csv

file=open('songs_list (3).csv')
type(file)

csvreader=csv.reader(file)

header=[]
header=next(csvreader)

flag=0
flag2=0

df=pd.read_csv (r'C:\Users\pc\Desktop\songs_list (3).csv')
#df=pd.DataFrame(data,columns=header) is used when we want to do only specific columns
print(df)

instrument1=input('Enter Instrument')
count1=int(input('Enter Number'))
choice=input('Want to Enter Another Instrument? (Y): ')
if(choice=='Y'):
    instrument2=input('Enter Instrument')
    count2=int(input('Enter Number'))
    for i in header:
           if(i==instrument1):
               flag=1
               break
           #elif(i==instrument2):
           #    flag2=1
    for j in header:
            if(j==instrument2):
                flag2=1
                break
    if(flag!=1 and flag2!=1):
           print('INSTRUMENT NOT PRESENT IN OUR DATABASE...')   
    else:      
           trial=df[(df[instrument1]==count1) & (df[instrument2]==count2)]
           print(trial)
else:
    for i in header:
           if(i==instrument1):
               flag=1
    if(flag!=1):
           print('INSTRUMENT NOT PRESENT IN OUR DATABASE...')
    else:      
           trial=df[(df[instrument1]==count1)]
           print(trial)
#trial=df[df[instrument1]==count1]
#instrument2=input('Enter Instrument')
#count2=int(input('Enter Number'))
#trial=df[(df[instrument1]==count1) & (df[instrument2]==count2)]
#print(trial)
