from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bkdb
from datetime import datetime, timedelta


cr_data = str(datetime.now() + timedelta(hours=3))[:19] 
options = webdriver.ChromeOptions()
#options.add_argument('--disable-extensions')
options.add_argument('--headless')
#options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def get_data_from_BCR():
    url='https://www.bcr.ro/ro/curs-valutar'
    driver.get(url)
    time.sleep(10)
    #driver.find_element_by_xpath('//*[@id="ACS-welcome"]/div[1]/div[4]/button[2]').click()
    #a = driver.find_element_by_xpath('//*[@id="ACS-welcome"]/div[1]/div[4]/button[2]')
    #print ("el : " + str(a.is_displayed()))
    #driver.find_element(By.XPATH,'//*[@id="ACS-welcome"]/div[1]/div[4]/button[2]').click()
    #time.sleep(3)

    nr=[1,2,3,4]
    name="BCR"
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[2]').text
        y=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[3]').text
        z=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[4]').text
        #print(name, x, y,z)
        bkdb.insert(name,x,y,z,cr_data)

def get_data_from_BT():
    url='https://www.bancatransilvania.ro/curs-valutar-spot/'
    driver.get(url)
    name="BT"
    nr=[1,2,3,4]
    for i in nr:
        x=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[1]/span').text
        y=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[3]').text
        z=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[4]').text
        bkdb.insert(name,x,y,z,cr_data)
        #print(name,x,y,z)

def get_data_from_Unicredit():
    driver.get('https://www.unicredit.ro/ro/institutional/Diverse/SchimbValutar.html')
    name="Unicredit"
    nr = [1,2,6,10]
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[1]/a/strong').text
        y=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[3]/div').text
        z=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[4]/div').text
        bkdb.insert(name,x[:3],y,z,cr_data)
        #print(name,x[:3],y,z)

def get_data_from_Raiffeisen():
    driver.get('https://www.raiffeisen.ro/persoane-fizice/curs-valutar/')
    name='Raiffeisen'
    nr=[0,1,2,3]
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[2]').text
        y=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[4]').text
        z=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[5]').text
        bkdb.insert(name,x,y,z,cr_data)
        #print(name,x,y,z)

def get_data_from_ING():
       r=requests.get("https://ing.ro/ing-in-romania/informatii-utile/curs-valutar")
       c=r.content
       soup=BeautifulSoup(c,"html.parser")
       monede=["EUR","USD","GBP","CHF"]
       name="ING"
       i=0
       for md in monede:
           all=soup.find_all("td",{"class":"buy","data-currency":md})
           y=all[1].text.replace(" ","").replace("\n","")
           all1=soup.find_all("td",{"class":"sell","data-currency":md})
           z=all1[1].text.replace(" ","").replace("\n","")
           all2=soup.find_all("td",{"class":"code"})
           x=all2[i].text.replace(" ","").replace("\n","")
           bkdb.insert(name,x,y,z,cr_data)
           #print(name,x,y,z)
           i+=1

#def get_data_from_ING():
#    url='https://ing.ro/ing-in-romania/informatii-utile/curs-valutar'
#    driver.get(url)
    #time.sleep(5)
#    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
    #time.sleep(5)
#    diver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[1]/ul/li[2]/a').click()
    #time.sleep(5)
#    name="ING"
#    nr = [1,2,3,4]
#    for i  in nr:
#        x=driver.find_element_by_xpath('//*[@id="exchange-second-tab"]/div/div[1]/table/tbody/tr['+str(i)+']/td[2]').text
#        y=driver.find_element_by_xpath('//*[@id="exchange-second-tab"]/div/div[1]/table/tbody/tr['+str(i)+']/td[4]').text
#        z=driver.find_element_by_xpath('//*[@id="exchange-second-tab"]/div/div[1]/table/tbody/tr['+str(i)+']/td[5]').text
#        print(name,x,y,z)

def get_data_from_BRD():
        url='https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta'
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="cookieConsentStickyFooter"]/div/div/div[2]/button').click()
        driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/p/a').click()
        name="BRD"
        nr = [2,3,4,11]
        for i in nr:
            x=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[2]/p['+str(i)+']').text
            y=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[4]/p['+str(i)+']').text
            z=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[5]/p['+str(i)+']').text
            bkdb.insert(name,x,y,z,cr_data)
            #print(name,x,y,z)


get_data_from_BT()
get_data_from_Unicredit()
get_data_from_Raiffeisen()
get_data_from_ING()
get_data_from_BRD()
get_data_from_BCR()

driver.close()
