from email.mime.text import MIMEText
import smtplib
from email.header import Header

msg = MIMEText('hello, send by python')
msg['Subject'] = '告警邮件'
from_addr = 'niejian9001@163.com'
password = 'ZQTHKDYFAZOUITOG'
to_addr = '393357255@qq.com'
send_server = 'smtp.163.com'
try:
    server = smtplib.SMTP_SSL(send_server, 465)

    # server.set_debuglevel(1)
    server.login(from_addr, password)
    msg['from'] = Header("Python邮件预警系统", 'utf-8')
    print(msg.as_string())

    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
except Exception as e:
    print('Faild:%s' % e)

