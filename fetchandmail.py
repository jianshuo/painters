import requests
from bs4 import BeautifulSoup
import yagmail

url = 'https://s.weibo.com/realtime?q=%236月16日起美暂停往返的中国民航航班%23&rd=realtime&tw=realtime&Refer=weibo_realtime'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

content = soup.find('p', {'class': 'txt'})
content = content.text.strip()
print(content)

author = soup.find('a', {'class': 'name'})
author = author.text
print(author)

mail = yagmail.SMTP('embarazada@qq.com', 'hlnixpqgqwwpbchd', 'smtp.qq.com')
mail.send('jianshuo@icloud.com', author + ' 发了一个微博，快去看看', content)
print('Mail sent')
