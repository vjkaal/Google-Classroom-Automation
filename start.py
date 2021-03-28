import webbrowser
from datetime import datetime
import csv

#webbrowser.open("www.google.com")

def time():
    now=datetime.now()
    hour=int(now.strftime("%H"))
    return (hour-8)


def day():
    today=datetime.today()
    return(today.weekday()+1)


with open('class.csv') as csvfile:
    row=day()
    row=5
    hour=time()
    print(hour)
    csvReader=csv.reader(csvfile,delimiter=',')
    i=0
    for rows in csvReader:
        i+=1
        if(i==row):
            if(hour>0 and hour<=8):
                print(rows[hour])
