import multiprocessing
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime
from bs4 import BeautifulSoup
import time
import requests
import threading
import sqlite3
import pandas as pd
from queue import Queue
import CreateDatabase

import os
class insertingMaching(threading.Thread):
    def __init__(self,queue,conn,cur,lock):
        threading.Thread.__init__(self)
        self.queue=queue
        df = pd.read_csv('AllCompanies.csv')
        self.stocks=df["Simbol"]
        self.conn=conn
        self.cur=cur
        self.lock=lock

        print("Thread by name: {}  has been initialized".format(self.getName()))




    def run(self):
        while(True):
            item=self.queue.get()
            if item=="quit":
                break

            ticker=item[1]
            if ticker=="ADRS-R-A":
                ticker="ADRS"
            elif ticker=="ADRS-P-A":
                ticker="ADRS2"
            else:
                ticker=ticker[:ticker.find("-")]
            #Find element
            if len(self.stocks[self.stocks==ticker])==0:
                continue
            print("Inserting {} at {} with {} ".format(ticker,item[0],self.getName()))
            string="INSERT INTO {} VALUES (\'{}\',{},{});".format(ticker,item[0],item[2].replace(",","."),item[3],item[4])
            self.lock.acquire(True)
            self.cur.execute(string)
            self.cur.execute("COMMIT;")
            self.lock.release()
            self.queue.task_done()





def ErsteDownloader(year):

    username="filip_macek@hotmail.com"
    password="2255123Filip"
    driver=webdriver.Firefox()
    driver.get('https://web.erstebroker.hr/login.aspx')

    #Typing username
    driver.find_element_by_id("ctl00_phLoginContent_txtUsername").click()
    driver.find_element_by_id("ctl00_phLoginContent_txtUsername").clear()
    driver.find_element_by_id("ctl00_phLoginContent_txtUsername").send_keys(username)

    #Typing password
    driver.find_element_by_id("ctl00_phLoginContent_txtPass").click()
    driver.find_element_by_id("ctl00_phLoginContent_txtPass").clear()
    driver.find_element_by_id("ctl00_phLoginContent_txtPass").send_keys(password)

    #Login
    driver.find_element_by_id('ctl00_phLoginContent_btnLogin').click()
    # WebDriverWait(driver,3).until(Ec.presence_of_all_elements_located(('id','mainMenu_DXI5_')))
    # driver.get('https://web.erstebroker.hr/pages/MarketTrades.aspx')

    WebDriverWait(driver,3).until(Ec.presence_of_all_elements_located(('id','mainMenu_DXI5_')))

    driver.get('https://web.erstebroker.hr/pages/MarketTrades.aspx')

    begin=datetime.datetime(year,1,1)
    end=datetime.datetime(year+1,1,1)
    end=end-datetime.timedelta(days=1)

    time.sleep(1)
    driver.implicitly_wait(2)
    # WebDriverWait(driver, 3).until(Ec.presence_of_all_elements_located(('id', 'ctl03_dateRange')))
    # driver.find_element_by_id('ctl03_dateRange').click()
    # driver.find_element_by_id('ctl03_dateRange').clear()
    # driver.find_element_by_id('ctl03_dateRange').send_keys(str(current_date.day)+"."+str(current_date.month)+"."+str(current_date.year))
    # driver.find_element_by_id('ctl03_dateRange').send_keys(Keys.ENTER)

    # table=driver.find_element_by_id('ctl03_gvMarketTrades_DXMainTable')
    # action=ActionChains(driver)
    # action.context_click(table).perform()
    # item=driver.find_element_by_id('ctl03_dateRange')
    data=[]
    ls=[]
    conn=sqlite3.connect("MarketData.db")
    cur=conn.cursor()
    df=pd.read_csv("AllCompanies.csv")
    stocks=df["Simbol"]

    for i in range((end-begin).days):

        time.sleep(0.5)
        current_date=begin+datetime.timedelta(days=i)
        if current_date.weekday() not in range(0,5):
            continue
        string_date=current_date.strftime("%d.%m.%Y")
        script="document.getElementById('ctl03_dateRange').value=\'{}\'".format(string_date)
        driver.execute_script(script)
        driver.find_element_by_id('ctl03_dateRange').send_keys(Keys.ENTER)
        time.sleep(1.5)
        #Lets calculate how many pages we got

        #Lets see mayybe it was a holiday,and there is no data: "Nema podataka za prikaz"
        result = driver.find_element_by_id('ctl03_gvMarketTrades_DXMainTable').get_attribute('innerHTML')
        time.sleep(1)
        if result.find("Nema podataka za prikaz")!=-1:
            continue
        driver.execute_script("document.getElementsByClassName(\"dxp-num\")[0].click();")
        time.sleep(1.5)
        result = driver.find_element_by_class_name("dxgvPagerBottomPanel_002").get_attribute('innerHTML')
        soup=BeautifulSoup(result,'lxml')
        x=soup.select('div >b:first-child')
        pages=x[0].text
        pages=pages[(pages.find('of')+3):]
        pages =int( pages[:pages.find(" ")])
        time.sleep(2)
        #Donwloading
        for t in range(0,pages):
            print(t)
            result=driver.find_element_by_id('ctl03_gvMarketTrades_DXMainTable').get_attribute('innerHTML')
            soup=BeautifulSoup(result,'lxml')
            temp=soup.select(".dxgvDataRow_002 >td")

            for item in temp:
                x=item.text
                if x.find("\n")!=-1:
                    x=x.replace(" ",'')
                    x=x.replace("\n","")
                if x=="ZSE.MTP":
                    ls=[]
                    continue

                if x=="ZSE.UT":
                    #Insert row ls into database
                    ticker = ls[1]
                    if ticker == "ADRS-R-A":
                        ticker = "ADRS"
                    elif ticker == "ADRS-P-A":
                        ticker = "ADRS2"
                    else:
                        ticker = ticker[:ticker.find("-")]
                    # Find element
                    if len(stocks[stocks == ticker]) == 0:
                        ls=[]
                        pass
                    else:
                        price=ls[2].replace(".","")
                        price=price.replace(',',".")
                        string = "INSERT INTO {} VALUES (\'{}\',{},{});".format(ticker, ls[0],price,ls[3], ls[4])
                        print(string)
                        cur.execute(string)
                        ls=[]
                else:
                    ls.append(x)
            cur.execute("COMMIT;")
            driver.execute_script("$(\'.dxWeb_pNext_002\').click()")
            time.sleep(1.4)



if __name__=="__main__":


    #os.remove('MarketData.db',)
    CreateDatabase.createPriceDatabases()

    time.sleep(1)

    ErsteDownloader(2010)
