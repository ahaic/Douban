

import smtplib

class oo(object):
    
    def sendmail(self):
        mail_server = "smtp.qq.com"
        send_from="562620123@qq.com"
        mail_to="hansoncao@hotmail.com"
        msg ="hello"
        mail = smtplib.SMTP(mail_server,timeosut = 10)
        mail.login("562620123@qq.com", "881025")
        mail.sendmail(send_from,mail_to,msg)
        print ("mail over")

pp=oo()
