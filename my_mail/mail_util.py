from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
from email.header import Header
import datetime


class MailUtil(object):

    # from_addr = 'niejian9001@163.com'
    # password = 'ZQTHKDYFAZOUITOG'

    @property
    def from_addr(self):
        return self._from_addr

    @from_addr.setter
    def from_addr(self, value):
        self._from_addr = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def to_addr(self):
        return self._to_addr

    @to_addr.setter
    def to_addr(self, value):
        self._to_addr = value

    @property
    def send_server(self):
        return self._send_server

    @send_server.setter
    def send_server(self, value):
        self._send_server = value

    def __init__(self):
        pass

    # 发送文本邮件
    def send_text_mail(self, subject, mail_content):
        try:
            msg = MIMEText(mail_content, 'plain', 'utf-8')
            msg['from'] = Header("Python邮件预警系统", 'utf-8')
            msg['From'] = 'system<' + self.from_addr + '>'
            msg['To'] = 'alter<' + self.to_addr + '>'
            msg['Subject'] = subject

            server = smtplib.SMTP(self.send_server, 25)
            server.login(self.from_addr, self.password)

            server.sendmail(self.from_addr, self.to_addr, msg.as_string())
            server.quit()
            print('send success')
        except Exception as e:
            print('邮件发送异常：%s' % e)

    """
    
    """

    def send_attachment_mail(self, subject, content, file_path):
        print("发送附件邮件")
        try:
            msg = MIMEMultipart()
            msg['from'] = Header("Python邮件预警系统", 'utf-8')
            msg['From'] = 'system<' + self.from_addr + '>'
            msg['To'] = 'alter<' + self.to_addr + '>'
            msg['Subject'] = subject
            # 邮件正文
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            with open(file_path, 'rb') as f:
                # 获取文件名，得到文件格式
                filename = f.name
                index = filename.rfind('.')
                index = int(index)
                print(isinstance(index, int))
                if index < 0:
                    print('轻选择一个正确的附件')
                    return
                # 文件后缀
                file_suffix = filename[index + 1: len(filename)]
                print(file_suffix)
                if None == file_suffix or len(file_suffix) <= 0:
                    print('轻选择一个正确的附件')
                    return

                # file_type = get_file_type(file_suffix)
                image_list = ['png', 'jpg', 'jpeg']
                file_type = 'image'
                if file_suffix in image_list:
                    file_type = 'image'
                else:
                    file_type = file_suffix

                filename_index = filename.rfind('/')
                if filename_index > 0:
                    filename = filename[filename_index + 1: len(filename)]

                # 设置附件的MIME和文件名，这里是png类型:
                mime = MIMEBase(file_type, file_suffix, filename=filename)

                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename=filename)
                mime.add_header('Content-ID', '0')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)

            server = smtplib.SMTP(self.send_server, 25)
            server.login(self.from_addr, self.password)
            print("prepare to send....")

            server.sendmail(self.from_addr, self.to_addr, msg.as_string())
            server.quit()
            print('发送附件成功')

        except Exception as e:
            print('邮件发送异常：%s' % e)


        """
        通过文件后缀获取文件类型
        jpg, jpeg, png --> image
        doc --> doc
        excel --> excel
        """
        def get_file_type(file_suffix):

            if file_suffix == 'png' or file_suffix == 'jpg' or file_suffix == 'jpeg':
                return 'image'

            return None