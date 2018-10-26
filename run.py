from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os
import attachments

app = Flask(__name__)


EmailLogin = 'test6974@outlook.com' 
EmailPassword = '5d}]VcPz88o(BB=f~u.<'

@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      result = request.form
      SetAttributes(result)
      return render_template("index.html")
    else:
        return render_template('index.html')


def SetAttributes(result):
    if result.get('attachments'):
        attachments.Generate(result['extension'],
                            result.get('minFileSize',1),
                            result.get('maxFileSize',10),
                            int(result['attachmentsPerEmail'])*int(int(result['totalToSend'])))
    SendEmail(result)
    attachments.Remove()

def SendEmail(result):
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('test6974@outlook.com', '5d}]VcPz88o(BB=f~u.<')

    for i in range(int(result['totalToSend'])):
        msg = EmailMessage()
        Subject = f"{result.get('subjectline','Subject')} {i}"
        msg['Subject'] = Subject
        msg.set_content("This is an automated email.")
        msg['From'] = 'test6974@outlook.com'
        msg['To'] = result['emailAddress']
        if result.get('attachments'):
            for j in range(1,int(result['attachmentsPerEmail'])):
                AttachmentFile = os.listdir('temp')
                MyAttachment = os.path.join('temp',AttachmentFile[0])
                with open(MyAttachment, 'rb') as content_file:
                    content = content_file.read()
                    msg.add_attachment(content, maintype='application/pdf', subtype='pdf', filename=AttachmentFile[0])
                    os.remove(MyAttachment)

        smtpObj.send_message(msg)

    smtpObj.quit()



if __name__ == "__main__":
    app.run(debug=True)