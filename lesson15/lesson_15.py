# import requests
# from bs4 import BeautifulSoup

# response = requests.get('http://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)
# print(response.json())

# url = 'http://jsonplaceholder.typicode.com/posts'
# data = {'title': 'foo', 'body': 'bar', 'userId': 1 }
# response = requests.post(url, json = data)
# print(response.status_code)
# print(response.json())

# url = 'http://jsonplaceholder.typicode.com/posts/1'
# data = {'title': 'updated', 'body': 'new bar', 'userId': 1 }
# response = requests.put(url, json = data)
# print(response.status_code)
# print(response.json())

# url = 'https://api.open-meteo.com/v1/forecast'
# params = {'latitude': 59.9343, 'longitude': 30.3353, 'current_weather': True}

# response = requests.get(url, params = params)

# if response.status_code == 200:
#     data = response.json()
#     print(data['current_weather']['temperature'])
# else:
#     print('error', response.status_code)

# url = 'https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F'

# headers = {}
# response = requests.get(url, headers)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.find('h1', {'id':'firstHeading'}).get_text())
# print(response.status_code)

# url = 'https://lenta.ru/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# all_news = soup.findAll('div', class_ = 'card-mini__text')
# filterd = []
# for data in all_news:
#     if data.find('div') is not None:
#         filterd.append(data.text)

# for data in filterd:
#     print(data[: -5], '\n')

