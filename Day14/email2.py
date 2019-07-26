#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 10:16
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : email2.py
# @Software   : PyCharm
# @Description: 发送带有附件的邮件


from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('test.jpg', 'rb') as f:
        jpg = MIMEText(f.read(), 'base64', 'utf-8')
        jpg['Content-Type'] = 'image/jpeg'
        jpg['Content-Disposition'] = 'attachment; filename=test.jpg'
        message.attach(jpg)

    # 创建SMTP对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全连接
    # smtper.starttls()
    sender = '1099420259@qq.com'
    receivers = ['xingfengwxx@gmail.com', '761074833@qq.com']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, 'cbckzmmdcxgjgbjg')
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('邮件发送完成！')


if __name__ == '__main__':
    main()
