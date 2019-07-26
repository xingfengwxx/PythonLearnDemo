#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 9:48
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : email1.py
# @Software   : PyCharm
# @Description: 发送电子邮件，SMTP服务


from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 发送者
    sender = '1099420259@qq.com'
    # 接受者
    receivers = ['xingfengwxx@gmail.com', '761074833@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('星爷', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 登录口令
    smtper.login(sender, 'cbckzmmdcxgjgbjg')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成！')


if __name__ == '__main__':
    main()
