# -*- coding: utf-8 -*-

import selenium
import csv
import requests
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from operator import itemgetter
from selenium.webdriver.common.action_chains import ActionChains
k2=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
k = [  'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
#with open('keywords.csv') as input:
 #   reader = csv.reader(input)
 #   k = []
 #   for f in reader:
 #       k.append(f[0])

locs=[]
with open('locations.csv') as input:
    row = csv.reader(input)
    for loc in row:
        loca = (loc[0])
        locs.append(loca)
cats=['Restaurant','Nightclubs',' Bar', 'Relaxation(Spa)', 'Cafes', 'Theme parksand water parks', 'Cinemas', 'Cafe' ,'Theaters']
cate=cats[2]

driver = webdriver.Firefox()
for keyword in locs:
    driver.get('https://www.google.lk/search?safe=off&q=+&npsic=0&rflfq=1&rlha=0&rllag=40758660,-73978906,2937&tbm=lcl&ved=0ahUKEwi-gpPPiY_XAhWBOJQKHQEFA_IQtgMIQw&tbs=lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:!1m3!1d35389.35656704087!2d-73.97447044999998!3d40.7492975!2m3!1f0!2f0!3f0!3m2!1i177!2i281!4f13.1;tbs:lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2')
    f=driver.find_element_by_id('lst-ib')
    f.send_keys(cate+ ' '+str(keyword+',London'))
    driver.find_element_by_id('_fZl').click()
    time.sleep(3)
    soup= BeautifulSoup(driver.page_source,'lxml')
    desc3 = ''
    sites1=[]
    sites2=[]
    names = []
    addrs = []
    maps=[]
    for h in soup.find_all('div',{'class':'_rl'}):
        names.append(h.text.encode('ascii','ignore'))
    for j in soup.find_all('a',{'class':'_jlf _Jrh'}):
        sites1.append(j['href'])
    for h in soup.find_all('span',{'class':'rllt__details lqhpac'}):
        try:
            addr =  h.contents[2].text.encode('UTF-8')
        except:
            addr=''
        addrs.append(addr)

    for f in soup.find_all('span',{'class':'rllt__details lqhpac'}):
        desc =(f.text.encode('UTF-8').split('+'))
    for o in soup.find_all('a', {'class': '_jlf _plf'}):
        ma = (o)
        map = 'https://www.google.com'+ma['href']
        maps.append(map)

        try:
            desc2 = desc[1].split('O')
            desc3 = desc2[0].encode('ascii','ignore')
            print 'error'
        except:
            desc3 = ''
        sites2.append(desc3)

    for i in xrange(0,len(sites1)):
        li =[]

        li.append(keyword.encode('ascii','ignore'))
        li.append(names[i].encode('ascii','ignore'))
        li.append(addrs[i].encode('ascii','ignore'))
        li.append(sites1[i].encode('ascii','ignore'))
        li.append(sites2[i].encode('ascii','ignore'))
        li.append(maps[i])

        print li
        resultFile = open(cate+".csv", 'ab')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(li)
        resultFile.close()

    nu=1
    no = 1
    while(nu==1):
        try:
            driver.find_element_by_css_selector('#pnnext > span:nth-child(2)').click()
            soup= BeautifulSoup(driver.page_source,'lxml')
            time.sleep(3)
            desc3 = ''
            sites1=[]
            sites2=[]
            names = []
            for h in soup.find_all('div',{'class':'_rl'}):
                names.append(h.text.encode('UTF-8'))
            for j in soup.find_all('a',{'class':'_jlf _Jrh'}):
                sites1.append(j['href'])
            for h in soup.find_all('span',{'class':'rllt__details lqhpac'}):
                try:
                    addr = h.contents[2].text.encode('UTF-8')
                except:
                    addr = ''
                addrs.append(addr)
            for f in soup.find_all('span',{'class':'rllt__details lqhpac'}):
                desc = (f.text.encode('UTF-8').split('+'))
            for o in soup.find_all('a', {'class': '_jlf _plf'}):
                ma = (o)
                map = 'https://www.google.com' + ma['href']
                maps.append(map)
                try:
                    desc2 = desc[1].split('O')
                    desc3 = desc2[0].encode('ascii','ignore')

                except:
                    desc3 = ''
                sites2.append(desc3)
            for i in xrange(0,len(sites1)):
                li =[]

                li.append(keyword.encode('ascii','ignore'))
                li.append(names[i].encode('ascii','ignore'))
                li.append(addrs[i].encode('ascii','ignore'))
                li.append(sites1[i].encode('ascii','ignore'))
                li.append(sites2[i].encode('ascii','ignore'))
                li.append(maps[i])
                print li
                resultFile = open(cate+".csv", 'ab')
                wr = csv.writer(resultFile, dialect='excel')
                wr.writerow(li)
                resultFile.close()
                time.sleep(4)
            no += 1
            if no == 5:
                nu=0
            time.sleep(5)
        except:
            nu=0
            print 'end'
            pass
