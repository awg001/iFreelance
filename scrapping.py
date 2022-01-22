import requests
from bs4 import BeautifulSoup as BS


url = 'https://freelance.habr.com/tasks?q=python'

res = requests.get(url)

jobs = []

if res.status_code == 200:
    soup = BS(res.content, 'html.parser')
    ul = soup.find('ul', id='tasks_list')
    li = ul.find_all('li', class_='content-list__item')
    for i in li:
        url = 'https://freelance.habr.com/' + i.a['href']
        title = i.a.text
        price = 'Договорная'
        if i.find('span', class_='count'):
            price = i.find('span', class_='count').text  
        views = i.find('span', class_='icon_task_views').text.strip() 
        responses = i.find('span', class_='icon_task_responses').text
        time = i.find('span', class_='icon_task_publish_at').text.strip()
        jobs.append({'url':url, 'title': title, 'price': price,
                    'views': views, 'responses': responses, 'time': time})



        
        
