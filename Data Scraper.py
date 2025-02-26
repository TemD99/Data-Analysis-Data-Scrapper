# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:04:55 2023

@author: Temitayo
"""


from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import requests

url = 'https://www.forbes.com/lists/ai50/?sh=5fa43e51290f'
page = requests.get(url)
page
soup = BeautifulSoup(page.text, 'html.parser')
header_content = soup.find_all('span', class_='header-content-text')
header_content
company_titles_tables = [title.text.strip() for title in header_content]
print(company_titles_tables)
import pandas as pd
df = pd.DataFrame(columns = company_titles_tables)
df
column_data = soup.find_all('div', class_='industry second table-cell what it does')
name = [item.text.strip() for item in soup.find_all('div', class_='organizationName first table-cell name')]
print(name)
what_it_does_data = [item.text.strip() for item in soup.find_all('div', class_='industry second table-cell what it does')]
print(what_it_does_data)
funding = [item.text.strip() for item in soup.find_all('div', class_='funding table-cell funding')]
print(funding)
head_quarters = [item.text.strip() for item in soup.find_all('div', class_='headquarters table-cell headquarters')]
print(head_quarters)
ceo = [item.text.strip() for item in soup.find_all('div', class_='ceoName table-cell ceo')]
print(ceo)
year_found = [item.text.strip() for item in soup.find_all('div', class_='yearFounded table-cell year founded')]
print(year_found)
employees = [item.text.strip() for item in soup.find_all('div', class_='employees table-cell employees')]
print(employees)
df['NAME'] = name
df['WHAT IT DOES'] = what_it_does_data
df['FUNDING'] = funding
df['HEADQUARTERS'] = head_quarters
df['CEO'] = ceo
df['YEAR FOUNDED'] = year_found
df['EMPLOYEES'] = employees
df
df.to_csv(r'C:\Users\Temitayo\Desktop\AI_Companies.csv', index = False)

