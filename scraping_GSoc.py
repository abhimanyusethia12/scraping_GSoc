#importing required libraries
import requests
from bs4 import BeautifulSoup
import csv
import re
import sys

#retrieving html script from the given URL 
URL = sys.argv[1]
page = requests.get(URL)

#making soup 
soup = BeautifulSoup(page.content,'html.parser')

#we need to use create 4 different lists because of the four different class names
section= soup.find('section',class_='lifted-section')
results1= section.find_all('div', class_='md-padding archive-project-card__header archive-project-card__header--mod-0')
results2= section.find_all('div', class_='md-padding archive-project-card__header archive-project-card__header--mod-1')
results3= section.find_all('div', class_='md-padding archive-project-card__header archive-project-card__header--mod-2')
results4= section.find_all('div', class_='md-padding archive-project-card__header archive-project-card__header--mod-3')

#function finds the required data and writes it in the csv file
def function(result, file):
    name= result.find('h4',class_='archive-project-card__student-name')
    divs = result.find_all('div')
    org_name= re.search(r'Organization: ([\w\s.-]+)', divs[1].text)
    rows= [name.text, org_name[1], divs[0].txt]
    csv_line = name.text.strip() + ', ' + org_name[1] + ', ' + divs[0].text + '\n'
    file.write(csv_line)

#running the loop over the different lists of results
with open('GSoc.csv','w',newline='',encoding='utf-8') as file:
    for result in results1:
        function(result, file)
    for result in results2:
        function(result, file)
    for result in results3:
        function(result, file)
    for result in results4:
        function(result, file)
    
    

        

