from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)


EmailLogin = 'EMAIL' 
EmailPassword = 'PASSWORD'

@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      result = request.form
      print (result)
      SetAttributes(result)
      return render_template("index.html")
    else:
        return render_template('index.html')


def SetAttributes(result):
    SendTo = result['emailAddress']
    NumberOfEmails = int(result['totalToSend'])
    if result['subjectLine']:
        subject = result['subjectLine']
    else:
        subject = 'Subject'
    if result.get('attachments'):
        numberOfAttachments = int(result['attachmentsPerEmail'])
        if result['fileExtension']:
            if result['fileExtension'] == 'mixed':
                fileExtension = ['.pdf','.txt','.doc','.csv','.xls','.jpg','.mp3']
            else:
                fileExtension  = result['fileExtension']
        if result['minFileSize']:
            minFileSize = result['minFileSize']
            maxFileSize = result['maxFileSize']
        else:
            minFileSize = 1
            maxFileSize = 10
    SendEmail(SendTo,subject,NumberOfEmails)


def SendEmail(to,subject,amount):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EmailLogin, EmailPassword)

    for i in range(amount):
        msg = EmailMessage()
        msg['Subject'] = subject + str(i)
        msg.set_content("This is an automated email.")
        msg['From'] = EmailLogin
        msg['To'] = to
        smtpObj.send_message(msg)

    smtpObj.quit()






if __name__ == "__main__":
    app.run(debug=True)