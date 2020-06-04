# Python也有App Store的。你可以安装然后使用
# 安装:在命令行里面输入：
#   pip3 install yagmail
# 使用的话，需要用
#   import yagmail

import yagmail

username = 'embarazada@qq.com'
password = 'hlnixpqgqwwpbchd'
server = 'smtp.qq.com'
mail = yagmail.SMTP(username, password, server)

to = 'jianshuo@icloud.com'
subject = 'How are you doing today?'
body = ['<h1>I kind of miss you. Do you want to reply me with some jokes?</h1>',
'<h2>其实今天早上睡个懒觉也不错</h2>',
'126.jpg']
mail.send(to, subject, body)
print('Msg sent to ' + to)
