import smtplib
from email.message import EmailMessage
import os

def SendEmail(InvoiceFolder):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('email', 'PASSWORD')
    MyInvoicePath = InvoiceFolder
    MyInvoice = os.listdir(MyInvoicePath)

    for i in MyInvoice:
        AttachmentFile = os.path.join(MyInvoicePath,i)
        Subject = i.split(" Invoice")[0]
        fName = i
        msg = EmailMessage()
        msg['Subject'] = Subject
        msg.set_content("This is an automated email.")
        msg['From'] = ''
        msg['To'] = ''
        with open(AttachmentFile, 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application/pdf', subtype='pdf', filename=fName)

        smtpObj.send_message(msg)

    smtpObj.quit()

SendEmail(r"C:\Users\Dan\Desktop\TestInvoices")


