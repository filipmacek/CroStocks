from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import codecs
import openpyxl
import urllib
import pandas as pd
import time
import threading
from queue import Queue
import os
import os.path
import requests
import sqlite3
import multiprocessing

def createPriceDatabases():
    conn=sqlite3.connect("MarketData.db")
    cur=conn.cursor()
    df=pd.read_csv("AllCompanies.csv",header=0)
    tickers=df["Simbol"]
    for stock in tickers:
        temp="CREATE TABLE IF NOT EXISTS [{}] (Date TEXT,Price REAL,Volume INTEGER)".format(stock)
        cur.execute(temp)



def ListOfAllCompenies():
    x=requests.get('https://www.zse.hr/default.aspx?id=26474')
    site=BeautifulSoup(x.content,'lxml')
    header=site.select('#dnevna_trgovanja > thead>tr>td')
    header=[x.text for x in header]
    header.append("url")

    #file=codecs.open('TrenutneDionice.csv','a',encoding="utf-8")

    list_of_All_Companies=[]
    for tr in site.select("#dnevna_trgovanja>tr"):
        x=[]
        #Simbol
        x.append(tr.find('td').text)
        #Izdavatelj
        x.append(tr.find("span").text)
        #ISIN
        x.append(tr.select('td')[2].text)
        #Broj izdanih
        x.append(tr.select('td')[3].text)
        #Nominala
        x.append(tr.select('td')[4].text)
        #Datum uvrstenja
        x.append(tr.select('td')[5].text)
        #url
        x.append("http://www.zse.hr/default.aspx"+tr.find('a').get('href'))
        list_of_All_Companies.append(x)
    data=pd.DataFrame(list_of_All_Companies,columns=header)
    data.to_csv("AllCompanies.csv",index=False)





class Downloader(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            rez=self.queue.get()
            if isinstance(rez,str) and rez == 'quit':
                break
            fdir, url = rez
            print("Downloading {} by Thread: {}".format(url,self.getName()))
            with open(fdir,'wb') as f:
                r=requests.get(url)
                f.write(r.content)
            print('{} downloaded'.format(url))
            self.queue.task_done()



def Crawler(ticker,url):
    homdir="D:\\ZSE\\"+ticker
    if not os.path.exists(homdir):
        os.makedirs(homdir)

    downloaders=[]

    queue=Queue()
    for i in range(5):
        dl=Downloader(queue)
        dl.start()
        downloaders.append(dl)
        print("Stavljam")

    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    for link in soup.findAll('a'):
        href=link.get('href')
        if href.startswith('userdocsimages/financ'):
            fdir=homdir+'\\'+href[href.find(ticker):]
            queue.put((fdir,"http://www.zse.hr/"+href))

    for i in range(5):
        queue.put('quit')
    for dl in downloaders:
        dl.join()
        print("PRINTAMMMM JOIN")



def rad():
    data=pd.read_csv(filepath_or_buffer="AllCompanies.csv",encoding="utf-8")
    url="https://www.zse.hr/default.aspx"+data.loc[0][data.shape[1]-1]
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    rez=soup.findAll('a',href=True)
    rezlist=[]
    for item in rez:
        if 'userdocsimages/financ' in item.get('href'):
            rezlist.append(item)


def checkForProperFinanSt(temp):
    #https://www.zse.hr/userdocsimages/financ/MAIS-fin2018-1Q-NotREV-K-HR.pdf
    pass

def main():
    df=pd.read_csv('AllCompanies.csv')
    p=multiprocessing.Pool(processes=(multiprocessing.cpu_count()-1))
    temp=[]
    for i in range(df.shape[0]):
        temp.append((df["Simbol"][i],df['url'][i]))

    temp=[(df["Simbol"][i],df['url'][i]) for i in df.shape()[0]]

    p.starmap_async(Crawler,temp)

if __name__=='__main__':
    main()