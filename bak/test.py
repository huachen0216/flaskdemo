from flask import Flask
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

from flask.ext.mail import Mail
from flask.ext.mail import Message
from threading import Thread

mail = Mail(app)

app.config['Mail_SERVER']='mail.yonyou.com'
app.config['MAIL_PORT']=25

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route("/mail")
def SendMail():
    msg = Message('test', sender='huachen0216@163.com', recipients=['huachen@yonyou.com'])
    msg.body = "text body"
    msg.html = "<b>HTML</b>body"
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return "OK"


