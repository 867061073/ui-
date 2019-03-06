#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '86706'
__mtime__ = '2019/3/5'
# qq:2456056533

佛祖保佑  永无bug!

"""
import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'   # 设置服务器，qq的SMTP服务host
mail_user = '382015144@qq.com'   # 发送的用户名（须修改）
mail_pwd = 'orwqmicutqhybiah'    # 此处为在qq开启SMTP服务时返回的密码 （须修改）


def send_email(content, mailto, get_sub): #内容，收件人，主题
    #'Setting MIMEText'
    msg = MIMEText(content.encode('utf8'), _subtype='html', _charset='utf8')#第一个参数是邮件正文，第二个参数是MIME的subtype（plain/html），最后一定要用utf-8编码保证多语言
    msg['From'] = mail_user    #发送人用户名
    msg['To'] = ",".join(mailto)   #收件人用户名
    msg['Subject'] = u'%s' % get_sub  # 主题

    try:
        #'connecting ', mail_host
        s = smtplib.SMTP_SSL(mail_host,465)    #smtp_ssl 端口465

        # s.connect(mail_host)

        #login to mail_host
        s.login(mail_user, mail_pwd)

        #send email
        s.sendmail(mail_user, mailto, msg.as_string())

        print('close the connection between the mail server')
        s.close()
    except Exception as e:
        print('Exception: ', e)

content='report201902271805.html'
to_list = ['867061073@qq.com', '403185295@qq.com']
send_email(content, to_list, 'hi xxx')
