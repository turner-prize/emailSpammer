from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os
import attachments

app = Flask(__name__)


EmailLogin = 'EMAIL' 
EmailPassword = 'PASSWORD'

@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      result = request.form
      print(result)
      SetAttributes(result)
      return render_template("index.html")
    else:
        return render_template('index.html')


def SetAttributes(result):
    SendTo = result['emailAddress']
    NumberOfEmails = int(result['totalToSend'])
    subject= result.get('subjectline','Subject')
    if result.get('attachments'):
        print("att")
        attachments.Generate(result['extension'],result.get('minFileSize',1),result.get('maxFileSize',10),int(result['attachmentsPerEmail']))
    #SendEmail(SendTo,subject,NumberOfEmails)
    attachments.Remove()

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