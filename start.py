import webbrowser
from datetime import datetime
import csv


def time():
    now=datetime.now()
    hour=int(now.strftime("%H"))
    return (hour-8)


def day():
    today=datetime.today()
    return(today.weekday()+1)


def getLink():
    link="noClass.html"
    with open('class.csv') as csvfile:
        #row=day()
        row=1
        #hour=time()
        hour=2
        #print(hour)
        csvReader=csv.reader(csvfile,delimiter=',')
        i=0
        for rows in csvReader:
            i+=1
            if(i==row):
                if(hour>0 and hour<=8):
                    link=str(rows[hour])
                    #print(link)
    return link

def main():
    link=getLink()
    #print(link)
    webbrowser.open(link)


main()