import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.thehindu.com/news/'

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    headlines = soup.find_all('h3')  
   
    extracted_data = []
    for headline in headlines:
        title = headline.get_text(strip=True)
        if title:  
            extracted_data.append([title])

    with open('news_headlines.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline']) 
        writer.writerows(extracted_data)

    print(f" Successfully saved {len(extracted_data)} headlines to 'news_headlines.csv'.")

else:
    print(f" Failed to retrieve content. Status code: {response.status_code}")
