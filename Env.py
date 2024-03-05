from  bs4 import BeautifulSoup
import requests
 
website = 'https://www.muyinteresante.com.mx/ciencia-y-tecnologia/'
results = requests.get(website)
content = results.text
 
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
 