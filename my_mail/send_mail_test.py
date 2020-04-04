# 同一路径下，直接引用相关文件名
import sys
import os
# 将文件加载到系统变量
sys.path.append(os.path.abspath("."))
# 引入相关信息
from my_mail.mail_util import MailUtil

# mail_util = MailUtil()
send_mail = MailUtil()
send_mail.to_addr = 'niejian9001@163.com'
# send_mail.to_addr = '393357255@qq.com'
send_mail.from_addr = 'niejian9001@163.com'
send_mail.send_server = 'smtp.163.com'
send_mail.password = 'ZQTHKDYFAZOUITOG'
# send_mail.send_text_mail('系统告警', 'python')
# send_mail.send_attachment_mail('附件邮件', '这时一个含有附件信息的邮件', '/Users/a/Desktop/cat-sql.png')
# send_mail.send_attachment_mail('附件邮件', '这时一个含有附件信息的邮件', '/Users/a/Desktop/Sentinel接入文档.pdf')
# send_mail.send_attachment_mail('附件邮件', '这时一个含有附件信息的邮件', '/Users/a/Desktop/复工证明申请模板.xlsx')
# send_mail.send_attachment_mail('附件邮件', '这时一个含有附件信息的邮件', '/Users/a/Desktop/复工证明(1).docx')
send_mail.send_attachment_mail('附件邮件', '这时一个含有附件信息的邮件', '/Users/a/Desktop/极简动态曲线通用PPT模板2.pptx')
