import smtplib
from email.message import EmailMessage
import os

def SendEmail():
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('test6974@outlook.com', '5d}]VcPz88o(BB=f~u.<')
    MyInvoicePath = InvoiceFolder
    MyInvoice = os.listdir(MyInvoicePath)

    #for i in :
        #AttachmentFile = os.path.join(MyInvoicePath,i)
        Subject = "test subject"#i.split(" Invoice")[0]
        #fName = i
        msg = EmailMessage()
        msg['Subject'] = Subject
        msg.set_content("This is an automated email.")
        msg['From'] = 'test6974@outlook.com'
        msg['To'] = 'dan@masonbreese.com'
        #with open(AttachmentFile, 'rb') as content_file:
        #    content = content_file.read()
        #    msg.add_attachment(content, maintype='application/pdf', subtype='pdf', filename=fName)

        smtpObj.send_message(msg)

    smtpObj.quit()

SendEmail()


