# DataScienceJobScrawper

Part I  Problem Framing 

Suppose the users of this web scraping application just like myself who want to find desirable and well-paid full-time jobs at a very competitive job market. it’s always good to have a machine to collect job posting information for you in time and automatically. Once some job postings that met user’s specific requirements, a personalized email alert will be sent to the users designated email addresses (could be one email address or an email list containing of server email addresses).

So, this application can save you time and efforts and always let you to be one of the earliest one who know the job opening information to provide you advantages at the job market. 

This simple python web scraping program is designed to collect job posting data and send alerts for job seekers. The specific example information as bellow.

     (a)   Job titles: Data Scientist       Data Analyst       Business Analyst
     (b)   Location: New York 
     (c)   Source Website: Indeed
     (d)   Alert receiving Email: Leiyang2586@gmail.com
     (e)   Alert sending Email: Ylei2@pride.hofstra.edu
     

Part II   Problem Solution 

Building a simple python scraping program that goes to Indeed website every day at 11:00 AM to scrape the first 30 pages of Indeed and send alert information once it finds wanted job posting data.
1. Tech Stack
     (a)  Windows 10
     (b)  Python 3.6
     (c)  Jupyter Notebook 
     (d)  Python Modules and Libraries: Beautifulsoup, Request, Re, CSV, Smtplib
     (e)  Related tech items: IBM cloud service Watson studio, Windows Task Scheduler, Regular Expression

2. Building Process
     (a)  Write a simple program V1 scrape one page 
     (b)  Define an advanced scraping program V2 with error handling function 
     (c)  Building a scraping list L containing the first 30 webpages of Indeed
     (d)  Write the data into CSV file after V2 scraped all the pages in L
     (e)  Improve V2 by adding job requirements filters.
     (f )  Create alert function by using Windows Task Scheduler or IBM could computing service  
