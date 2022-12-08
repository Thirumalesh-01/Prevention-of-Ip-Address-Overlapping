from flask import Flask
from flask import request
from flask import render_template
from flask_mail import Mail, Message
import smtplib
from random import randint
import math
from flask_migrate import migrate, Migrate

otp = randint(12000,30333);
app = Flask(__name__)

app.app_context().push()
mail = Mail(app)
mail2 = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thirumalesh1602@gmail.com'
app.config['MAIL_PASSWORD'] = 'uzuqwjhrspjwteln'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
mail2 = Mail(app)

@app.route('/' ,methods = ['get','post'])
def start():
    return render_template('index.html')

@app.route('/authint', methods = ['get','post'])
def authint():
    username = (request.args.get('username'))
    password = (request.args.get('password'))
    msg = Message(
        'Confirmation Using the OTP',
        sender='thirumalesh1602@gmail.com',
        recipients=[username]
    )

    secretkey = "XcYtuGys";
    msg.body = ("OTP to Login In Website: " + str(otp))
    mail.send(msg)
    return render_template('authentic.html')



@app.route("/authentication",methods=['get','post'])
def authentication():
    username = request.args.get("username");
    password = request.args.get("password");
    otper = int(request.args.get("otper"));
    if (otper == otp and password == 's@rk@r@mb'):
     return render_template('front.html')
    else:
        return render_template('error.html')


@app.route('/basics' , methods = ['get','post'])
def basics():
    userpers = request.args.get('userpers')
    userpers = int(userpers)
    return render_template("basic.html", userpers=userpers)

@app.route('/inputvalues', methods = ['get','post'])
def inputvalues():
   num = (request.args.get('totals'))
   import ipaddress
   a = 0
   ipadd = []
   l = []
   num = int(num);
   for i in range(num):
       i = str(i)
       ipadd.append(ipaddress.ip_network(request.args.get("first"+i)))

   # ipadd.append(ipaddress.ip_network(request.args.get("first1")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first2")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first3")))
   # /ipadd.append(ipaddress.ip_network(request.args.get("first4")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first5")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first6")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first7")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first8")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first9")))
   # ipadd.append(ipaddress.ip_network(request.args.get("first10")))
   num = int(num);
   res = ""
   for x in ipadd:
        res += str(x)+"\n";
   def binary(x, y):
    if (x.overlaps(y)):
        l.append(1)
        p = 1
        return p
    else:
     l.append(0)
   def overlap(ip):
     for i in range(0, num):
          for j in range(i+1, num):
             q = binary(ip[i], ip[j])
             if q == 1:
               a = i
     return l
   k = overlap(ipadd)
   while True not in k:
    for i in range(0, num):
      ipadd[i] = ipadd[i].supernet(prefixlen_diff=1)
    k = overlap(ipadd)
   para =   "minimum subnet mask required to avoid ip overlapping greater than"
   broadcastvalue = ipadd[a].broadcast_address
   para2 ="with broadcast address"
   print(
    "minimum subnet mask required to avoid ip overlapping greater than", ipadd[a])
   print('with broadcast address', ipadd[a].broadcast_address)
   msg = Message(
       'The Appropiate Subnet Mask',
       sender='thirumalesh1602@gmail.com',
       recipients=['thirumalesh1602@gmail.com']
   )
   msg.body = 'minimum subnet mask required to avoid ip overlapping greater than ' + str(ipadd[a]) +" with broadcast address " + str(ipadd[a].broadcast_address) +" for the user given ipaddresses\n" +res
   mail.send(msg)
   return render_template('inputvalues.html' ,para = para,ipadd = ipadd[a],para2 = para2,broadcastvalue=broadcastvalue)


@app.route('/randomip',methods=['get','post'])
def randomip():
    return render_template('randomip.html')

#=--------------->>>> DATABASE CONNECTIVITY WITH FLASK----->>>>>>>\

import  os;
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname((__file__)))
# trying, to grab the absolute path of the currrent file which we are working !!
#-->> os library, helps, us to get the correct position, of it!!

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
###################
Migrate(app,db)
class Register(db.Model):
    __tablename__ = "registers"

    id = db.Column(db.Integer,primary_key = True)
    #-->>> try to have the onecolumn to be the uniquely identifier for all!!
    name  = db.Column(db.Text)
    age = db.column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):#-->> which gives string representtion
        return f"Hello {self.name } of age {self.age } is registered"


if(__name__=="__main__"):
   app.run(debug=True)


