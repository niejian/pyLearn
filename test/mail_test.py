# 同一路径下，直接引用相关文件名
import sys
import os
sys.path.append(os.path.abspath("."))

from my_mail.mail_util import MailUtil

send_mail = MailUtil()
# send_mail = mail_util.MailUtil()
send_mail.to_addr = '393357255@qq.com'
send_mail.from_addr = 'niejian9001@163.com'
send_mail.send_server = 'smtp.163.com'
send_mail.password = 'ZQTHKDYFAZOUITOG'
send_mail.send_text_mail('系统告警', 'python告警邮件')

