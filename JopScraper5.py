#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# develop a simple program to scrape one sigle page on Indeed

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

web_address = 'https://www.indeed.com/jobs?q=business+analyst%2Cdata+analyst%2Cdata+scientist&l=New+York%2C+NY&start='
html = urlopen(web_address)
bs = BeautifulSoup(html.read(),'html.parser')
Jobs = bs.find_all('div',{'class':'jobsearch-SerpJobCard'}) 

Joblist=[]
for Job in Jobs:
    JobTitle = Job.find('a',{'data-tn-element':'jobTitle'})
    if JobTitle==None:
        JobTitle=Job.find('h2',{'class':'jobtitle'}) 
    if JobTitle !=None:
        Title=JobTitle.get_text().strip('\n')
    else:
        Title='TitleMissing'
    
    Jobcompany = Job.find('span',{'class':'company'})
    if Jobcompany !=None:
        Company=Jobcompany.get_text().lstrip()
    else:
        Company='NocompanyName'
        
    Joblocation = Job.find('span',{'class':'location'})
    if Joblocation==None:
        Joblocation = Job.find('div',{'class':'location'})
    if Joblocation !=None:
        Location=Joblocation.get_text()
    else:
        Location='NoLocation'
    
    JobSalary = Job.find('span',{'class':'salary no-warp'})
    if JobSalary != None:
        Salarytext = JobSalary.get_text().lstrip('\n')
        Salary = re.findall(r'\$[0-9.,-]+',Salarytext)
    else:
        Salary = 'Notavaliable'
        
    Jobpostdate = Job.find('span',{'class':'date'})
    if Jobpostdate!=None:
        Date=Jobpostdate.get_text()
    else:
        Date='NoDate'
           
    Jobmatch = Job.find('div',{'class':'serp-ResumeMatch-heading'})
    if Jobmatch !=None:
        Matcha = Jobmacth.get_text()
    else:
        Match = 'TBD'
    
    JobviewerNumbers = Job.find('span',{'class':'slNoUnderline'})
    if JobviewerNumbers != None:
        Number = JobviewerNumbers.get_text()     
    else:
        Number = "NotDisplayed"
    
    
        
        new_Job = [Title,Company,Location,Date,Salary,Match,Number]
        
        print(new_Job)
        Joblist.append(new_Job)
# print the list as well
print('------------------------------Below is the list and Well Done---------------------------------')
print(Joblist)
len(Joblist)


# In[ ]:


# write the results of the first page in a CSV file named 'JobScraper_CSV'.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

with open('JobScraper.csv','w',newline='') as myFile:
    writer = csv.writer(myFile)
    writer.writerow(["Title","Company","Location","Date","Match","Numberstext"])


web_address = 'https://www.indeed.com/jobs?q=business+analyst%2Cdata+analyst%2Cdata+scientist&l=New+York%2C+NY&start='
html = urlopen(web_address)
bs = BeautifulSoup(html.read(),'html.parser')
Jobs = bs.find_all('div',{'class':'jobsearch-SerpJobCard'}) 

Joblist=[]
for Job in Jobs:
    JobTitle = Job.find('a',{'data-tn-element':'jobTitle'})
    if JobTitle==None:
        JobTitle=Job.find('h2',{'class':'jobtitle'}) 
    if JobTitle !=None:
        Title=JobTitle.get_text().strip('\n')
    else:
        Title='TitleMissing'
    
    Jobcompany = Job.find('span',{'class':'company'})
    if Jobcompany !=None:
        Company=Jobcompany.get_text().lstrip()
    else:
        Company='NocompanyName'
        
    Joblocation = Job.find('span',{'class':'location'})
    if Joblocation==None:
        Joblocation = Job.find('div',{'class':'location'})
    if Joblocation !=None:
        Location=Joblocation.get_text()
    else:
        Location='NoLocation'
    
    Jobpostdate = Job.find('span',{'class':'date'})
    if Jobpostdate!=None:
        Date=Jobpostdate.get_text()
    else:
        Date='NoDate'
           
    Jobmatch = Job.find('div',{'class':'serp-ResumeMatch-heading'})
    if Jobmatch !=None:
        Matcha = Jobmacth.get_text()
    else:
        Match = 'TBD'
    
    JobviewerNumbers = Job.find('span',{'class':'slNoUnderline'})
    if JobviewerNumbers != None:
        Number = JobviewerNumbers.get_text()     
    else:
        Number = "NotDisplayed"
    
    
        
        new_Job = [Title,Company,Location,Date,Match,Number]
        print(new_Job)
        Joblist.append(new_Job)
        
with open('JobScraper.csv','a',newline='',encoding='utf-8') as myFile:
    writer = csv.writer(myFile)
    writer.writerows(Joblist)


# In[ ]:


# creat the list of URL's for the most recent 100 jobposting pages

baseURL='https://www.indeed.com/jobs?q=business+analyst%2Cdata+analyst%2Cdata+scientist&l=New+York%2C+NY&start='

urlList=[]
for i in range(0,1001,10):
    newURL=baseURL + str(i)
    urlList.append(newURL)

print(urlList[0:50])
len(urlList)


# In[ ]:


# convert the scraping into a function so that we can it on different pages. The JobScraper function takes the page number(0,10,20,30,...) as input and returns a list of all the Jobs on the page in a list of lists format

def JobScraper(pageNumber):
    
    baseURL = 'https://www.indeed.com/jobs?q=business+analyst%2Cdata+analyst%2Cdata+scientist&l=New+York%2C+NY&start='
    url = baseURL + str(pageNumber)
    html = urlopen(web_address)
    bs = BeautifulSoup(html.read(),'html.parser')
    Jobs = bs.find_all('div',{'class':'jobsearch-SerpJobCard'}) 

    Joblist=[]
    for Job in Jobs:
        
        JobTitle = Job.find('a',{'data-tn-element':'jobTitle'})
        if JobTitle==None:
            JobTitle=Job.find('h2',{'class':'jobtitle'}) 
        if JobTitle !=None:
            Title=JobTitle.get_text().strip('\n')
        else:
            Title='TitleMissing'
    
        Jobcompany = Job.find('span',{'class':'company'})
        if Jobcompany !=None:
            Company=Jobcompany.get_text().lstrip()
        else:
            Company='NocompanyName'
        
        Joblocation = Job.find('span',{'class':'location'})
        if Joblocation==None:
            Joblocation = Job.find('div',{'class':'location'})
        if Joblocation !=None:
            Location=Joblocation.get_text()
        else:
            Location='NoLocation'
    
        Jobpostdate = Job.find('span',{'class':'date'})
        if Jobpostdate!=None:
            Date=Jobpostdate.get_text()
        else:
            Date='NoDate'
           
        Jobmatch = Job.find('div',{'class':'serp-ResumeMatch-heading'})
        if Jobmatch !=None:
            Match = Jobmacth.get_text()
        else:
            Match = 'TBD'
    
        JobviewerNumbers = Job.find('span',{'class':'slNoUnderline'})
        if JobviewerNumbers != None:
            Numberstext = JobviewerNumbers.get_text()     
        else:
            Number = "NotDisplayed"
    
    
        
        new_Job = [Title,Company,Location,Date,Match,Numberstext]
        print(new_Job)
        Joblist.append(new_Job)
        
    return Joblist  


# In[ ]:


JobScraper(200)


# In[ ]:


# haddle errors to make the code more robust

from urllib.error import HTTPError
from urllib.error import URLError

def JobScraperwithExceptions(pageNumber):
    print('*** Scraping Jobs on page:',int(pageNumber/10 + 1),'***\n\n')
    
    baseURL = 'https://www.indeed.com/jobs?q=business+analyst%2Cdata+analyst%2Cdata+scientist&l=New+York%2C+NY&start='
    url = baseURL + str(pageNumber)
    
    try:
        
        html = urlopen(url)
        
    except HTTPError as e1:
        print('HTTP request was not responsed')
        print('---------------------HTTPError---------------------------')
        return None
    except URLError as e2:
        print('URL can not be opened')
        print('---------------------URLError----------------------------')
        
    bs = BeautifulSoup(html.read(),'html.parser')
    
    try:
        
        Jobs = bs.find_all('div',{'class':'jobsearch-SerpJobCard'}) 
        
    except AttributeError as e3:
        print('Tag was not found')
        print('-------------------AttributeError-----------------------')
        
    else:
        
        Joblist = []
        
        for Job in Jobs:
            
            JobTitle = Job.find('a',{'data-tn-element':'jobTitle'})
            if JobTitle==None:
                JobTitle=Job.find('h2',{'class':'jobtitle'}) 
            if JobTitle !=None:
                Title=JobTitle.get_text().strip('\n')
            else:
                Title='TitleMissing'
            
            Jobcompany = Job.find('span',{'class':'company'})
            if Jobcompany !=None:
                Company=Jobcompany.get_text().lstrip()
            else:
                Company='NocompanyName'
            
            Joblocation = Job.find('span',{'class':'location'})
            if Joblocation==None:
                Joblocation = Job.find('div',{'class':'location'})
            if Joblocation !=None:
                Location=Joblocation.get_text()
            else:
                Location='NoLocation'
            
            Jobpostdate = Job.find('span',{'class':'date'})
            if Jobpostdate!=None:
                Date=Jobpostdate.get_text()
            else:
                Date='NoDate'
            
            Jobmatch = Job.find('div',{'class':'serp-ResumeMatch-heading'})
            if Jobmatch !=None:
                Match = Jobmacth.get_text()
            else:
                Match = 'TBD'
            
            JobviewerNumbers = Job.find('span',{'class':'slNoUnderline'})
            if JobviewerNumbers != None:
                Numberstext = JobviewerNumbers.get_text()
            else:
                Number = "NotDisplayed"
                
            
                new_Job = [Title,Company,Location,Date,Match]
            
                Joblist.append(new_Job)
            
        return Joblist


# In[ ]:


JobScraperwithExceptions(30)


# In[ ]:


# run the function in a loop and write the results into a csv file

with open('JobScraper_Jobs_Final.csv','w',newline='') as myJobsFile:
    writer = csv.writer(myJobsFile)
    writer.writerow(["Title","Company","Location","Date","Match"])
    
with open('JobScraper_Jobs_Final.csv','a',newline='',encoding='utf-8') as myJobsFile:
    writer =csv.writer(myJobsFile)
    Joblist=[]
    for i in range(0,301,10):
        Joblist = JobScraperwithExceptions(i)
        writer.writerows(Joblist)
        
print('-----------------Yes you made it------------------- ')
print('-------------Screpting has finished---------------- ')
print('---------Data has been writen into file------------ ')
print('-----------------You are awesome!------------------ ')

