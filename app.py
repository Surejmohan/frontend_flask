from flask import Flask,render_template,flash, redirect,url_for,session,logging,request,Response
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm 
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired



IDPROOF_FOLDER = './ID_Proof'
ALLOWEDID_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app =Flask(__name__)
mail=Mail(app)
s = URLSafeTimedSerializer('secret')

app = Flask(__name__)
app.config['IDPROOF_FOLDER'] = IDPROOF_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret'



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'pinpoint.four.2020@gmail.com'
app.config['MAIL_PASSWORD'] = 'Google2020'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



def allowed_file3(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWEDID_EXTENSIONS




db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(50),unique=True, nullable=False,primary_key=True)
    password = db.Column(db.String(15),nullable=False)
    type = db.Column(db.String(15),nullable=False)

    def __init__(self,username,password,type):
        self.username=username
        self.password=password
        self.type=type
    
class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    admin_id=db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,fname,lname,phone,mail,admin_id):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.admin_id=admin_id 
        
class Authority(db.Model):
    __tablename__ = 'Authority'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(50))
    job = db.Column(db.String(50))
    proof=db.Column(db.String(40))
    confirm=db.Column(db.Boolean,unique=False, default=False)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,job,proof,confirm):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.job=job
        self.proof=proof 
        self.confirm=confirm

class Ordinary(db.Model):
    __tablename__ = 'Ordinary'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(30))
    state = db.Column(db.String(30))
    city = db.Column(db.String(30))
    proof=db.Column(db.String(40))
    address=db.Column(db.String(50))
    zip = db.Column(db.Integer)
    confirm=db.Column(db.Boolean,unique=False, default=False)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,state,city,address,zip,proof,confirm):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.state=state
        self.proof=proof    
        self.address=address
        self.city=city
        self.zip=zip
        self.confirm=confirm


class Other(db.Model):
    __tablename__ = 'Other'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    admin_approval = db.Column(db.String(5))
    admin_id =  db.Column(db.Integer)
    no_of_video_upload = db.Column(db.Integer)
    no_of_video_request = db.Column(db.Integer)
    third_party_issue_id = db.Column(db.Integer)
    third_party_pending_order = db.Column(db.String(10))
    third_party_response = db.Column(db.String(20))  #video not available or available
    date= db.Column(db.String(20))
    start_time = db.Column(db.String(20))
    end_time = db.Column(db.String(20))
    live_recording_no=db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,admin_approval,admin_id,no_of_video_upload,no_of_video_request,third_party_issue_id,third_party_pending_order,third_party_response,date,start_time,end_time,live_recording_no,usr_name):
        self.admin_approval=admin_approval
        self.admin_id=admin_id
        self.no_of_video_request=no_of_video_upload
        self.third_party_issue_id=third_party_issue_id
        self.third_party_pending_order=third_party_pending_order
        self.third_party_response=third_party_response
        self.date=date    
        self.start_time=start_time
        self.end_time=end_time
        self.live_recording_no=live_recording_no
        self.usr_name=usr_name


    



class Third(db.Model):
    __tablename__ = 'Third'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    dept = db.Column(db.String(50))
    name = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    Third_party_id = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,dept,name,mail,third_party_id,phone):
        self.usr_name=usr_name
        self.dept=dept
        self.name=name
        self.phone=phone
        self.mail=mail
        self.third_party_id=third_party_id
        



@app.route('/register', methods=['GET','POST'])
def Register():
     if request.method == 'POST':
         fname = request.form['firstname']
         lname = request.form['lastname']
         username = request.form['username']
         password = request.form['password']
         confpassword = request.form['confpassword']
         phone = request.form['mobile']
         email = request.form['mail']
         address = request.form['address']
         state = request.form.get('state')
         city = request.form.get('city')
         zip = request.form['zipcode']
         file1 = request.files['idproof']
         proof = file1.filename
         exists = User.query.filter_by(username=username).first()
         if not exists:
            if(password == confpassword):
                reg = User(username = username,password = password,type = 'Ordinary')
                db.session.add(reg)

                ord = Ordinary(fname = fname, lname = lname, phone = phone, mail = email, state = state,
                city = city,proof = proof, address = address, zip = zip, usr_name = username,confirm=0)
                db.session.add(ord)
                
                db.session.commit()
                #confirmation mail
                token = s.dumps(email, salt='email-confirm')

                msg = Message('Confirm PINPOINT Account', sender = 'pinpoint.four.2020@gmail.com', recipients = [email])
                link = url_for('confirm_email', token=token, _external=True)
                msg.html = render_template('email.html',link=link)
                mail.send(msg)

                
                if file1 and allowed_file3(file1.filename):
                    filename = secure_filename(file1.filename)
                    filename = username +'_' + filename 
                    file1.save(os.path.join(app.config['IDPROOF_FOLDER'], filename))
                    return '<html><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><center><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><h1>Please Confirm Your Email Address</h1></div><div class="card-body"><br><p class="card-text">We have sent an email with a confirmation link to your email address. In order to complete the sign-up process, please click the confirmation link.<br><br>If you do not receive a confirmation email, please check your spam folder. Also, please verify that you entered a valid email address in our sign-up form.</p><br><br></div> </div><br><br><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><br><h4>Your Documents are sent to admin for Verification.After verification your account will be activated.<BR> Please wait for the account activation mail</h4></p><br><br></div></html>'
            else:
                flash('Password and Confirm password not matched','error')
                return render_template('index.html',scroll='re')


     else:
         flash('Username already taken,try somethig else','error')
         return render_template('index.html',scroll='re')
             

    
         

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=172800)
    except SignatureExpired:
        return '<h1>The link is expired!</h1>'
    Ord = Ordinary.query.filter_by(mail=email).first()
    Ord.confirm = 1
    db.session.add(Ord)
    db.session.commit()
    return '<h1>Your email is verifed!</h1>'

@app.route('/reg_official', methods=['GET','POST'])
def Register2():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        username = request.form['uname']
        password = request.form['password']
        confpassword = request.form['confpassword']
        phone = request.form['mobile']
        email = request.form['email']
        job = request.form['job']
        department = request.form['department']
        file1 = request.files['jobproof']
        proof = file1.filename
        if job == 'Other':
            job = department
        exists = User.query.filter_by(username=username).first()
        if not exists:
            if(password == confpassword):
                
                reg = User(username = username,password = password,type = 'Authority')
                db.session.add(reg)

                Auth = Authority(fname = fname, lname = lname, phone = phone, mail = email, proof = proof, job=job , usr_name = username,confirm=0)
                db.session.add(Auth)
                
                db.session.commit()
                #confirmation mail
                token = s.dumps(email, salt='email-confirm')
                msg = Message('Confirm PINPOINT Account', sender = 'pinpoint.four.2020@gmail.com', recipients = [email])
                link = url_for('confirm_email', token=token, _external=True)
                msg.html = render_template('email.html',link=link)
                mail.send(msg)
                
                if file1 and allowed_file3(file1.filename):
                    filename = secure_filename(file1.filename)
                    filename = username +'_' + filename 
                    file1.save(os.path.join(app.config['IDPROOF_FOLDER'], filename))
                    return '<html><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><center><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><h1>Please Confirm Your Email Address</h1></div><div class="card-body"><br><p class="card-text">We have sent an email with a confirmation link to your email address. In order to complete the sign-up process, please click the confirmation link.<br><br>If you do not receive a confirmation email, please check your spam folder. Also, please verify that you entered a valid email address in our sign-up form.</p><br><br></div> </div><br><br><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><br><h4>Your Documents are sent to admin for Verification.After verification your account will be activated.<BR> Please wait for the account activation mail</h4></p><br><br></div></html>'
            else:
                flash('Password and Confirm password not matched','error')
                return render_template('index.html',scroll='re')

        else:
            
            flash('Username already taken,try somethig else','error')
            return render_template('index.html',scroll='re')
        


            
@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        passw = request.form['psw']
        
        login = User.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            #return redirect(url_for("index"))
            return 'done'

      
            
            







@app.route('/')
def index():
    #return '<html><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><center><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><h1>Please Confirm Your Email Address</h1></div><div class="card-body"><br><p class="card-text">We have sent an email with a confirmation link to your email address. In order to complete the sign-up process, please click the confirmation link.<br><br>If you do not receive a confirmation email, please check your spam folder. Also, please verify that you entered a valid email address in our sign-up form.</p><br><br></div> </div><br><br><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><br><h4>Your Documents are sent to admin for Verification.After verification your account will be activated.<BR> Please wait for the account activation mail</h4></p><br><br></div></html>'
    return render_template('index.html')



if(__name__ == "__main__"):
    app.run(debug=True)
