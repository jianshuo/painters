import requests
from bs4 import BeautifulSoup


resp = requests.get('https://s.weibo.com/realtime?q=%23姜潮妈妈婚前给麦迪娜买房%23&rd=realtime&tw=realtime&Refer=weibo_realtime')
soup = BeautifulSoup(resp.text, 'html.parser')
card = soup.find('div', attrs={'class': 'card-wrap'}).find('p', attrs={'class':'txt'})
latest = card.text.replace(' ', '').replace('\n', '')
