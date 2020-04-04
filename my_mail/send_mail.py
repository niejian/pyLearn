from email.mime.text import MIMEText
import smtplib
from email.header import Header

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = 'python 告警邮件'
from_addr = 'niejian9001@163.com'
password = 'ZQTHKDYFAZOUITOG'
to_addr = '393357255@qq.com'
# to_addr = 'niejian9001@163.com'
msg['From'] = 'system<'+from_addr+'>'
msg['To'] = 'alter<'+to_addr+'>'
send_server = 'smtp.163.com'
try:
    server = smtplib.SMTP(send_server, 25)
    # server.set_debuglevel(1)
    server.login(from_addr, password)
    msg['from'] = Header("Python邮件预警系统", 'utf-8')
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print('send success')
except Exception as e:
    print("发生异常：%s" % e)