

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import time as time

# Provide the Chromedriver executable path as a string
chromedriver_path = r'D:\\chrome-win64'

# Create a ChromeService instance with the executable path
service = ChromeService(executable_path=chromedriver_path)
service.start()

# Use the service to create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service)

CourseCode = []  
Title= []  
Description = []  
Instructor=[]


web="http://eduko.spikotech.com"


driver.get("http://eduko.spikotech.com")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
links=[]
for div in soup.findAll("div",attrs={"class":"card-body text-center"}):
    anchor=div.find('a',href=True)
    if anchor:
        link=anchor["href"]
        links.append(link)
print(links)
for link in links:
    link= web + link
    driver.get(link) 
    time.sleep(10)  
    pageContent=driver.page_source
    pageSoup = BeautifulSoup(pageContent, features="html.parser")   

for a in soup.findAll('div', class_='card-body text-center'):
    name=a.find('h4',class_={'class':'card-title'})
    code=a.find('div',class_={'id':'CourseCode'})
    Descr=a.find('p',class_='card-text')
    title=a.find('h4',class_={'class':'card-title'})
    Inst=a.find('h7')
    

    
    if(code!= None):
     CourseCode.append(code.text)
    else:
     CourseCode.append("None")  
    if(name!= None):
     Title.append(name.text)
    else:
      Title.append("None")   
    if(Descr!= None):
     Description.append(Descr.text)
    else:
     Description.append("None")    
    if(Inst!= None):
     Instructor.append(Inst.text)
    else:
     Instructor.append("None")   
         
     
     
df = pd.DataFrame({'CourseCode': CourseCode, 'Title': Title, 'Description': Description,'Instructor':Instructor})
df.to_csv('EDUKO.csv', index=False, encoding='utf-8')

# Close the browser and the service
driver.quit()
service.stop()


