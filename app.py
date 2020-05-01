from flask import Flask,render_template,flash, redirect,url_for,session,logging,request,Response
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm 
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from random import seed
from random import randint
from flask.helpers import send_from_directory
from datetime import timedelta
# seed random number generator
seed(1)
# generate some integers

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

app.secret_key = "hello"



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
    
#Admin Table
class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    admin_id = db.Column(db.String(20))
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,fname,lname,phone,mail,admin_id):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.admin_id=admin_id 
        
#Authority Table
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


#Ordinary Table
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


#Other Table
class Other(db.Model):
    __tablename__ = 'Other'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    admin_approval = db.Column(db.String(5))
    admin_id =  db.Column(db.String(20))
    no_of_video_upload = db.Column(db.Integer)
    no_of_video_request = db.Column(db.Integer)
    third_party_issue_id = db.Column(db.String(20)) 
    third_party_pending_order = db.Column(db.String(10))
    third_party_response = db.Column(db.String(20))  #video available or not
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


#Third table
class Third(db.Model):
    __tablename__ = 'Third'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    dept = db.Column(db.String(50))
    name = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    third_party_id = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,dept,name,mail,third_party_id,phone):
        self.usr_name=usr_name
        self.dept=dept
        self.name=name
        self.phone=phone
        self.mail=mail
        self.third_party_id=third_party_id


#Count table
class Count(db.Model):
    __tablename__ = 'Count'
    id = db.Column(db.Integer, primary_key=True)
    Ordinary = db.Column(db.Integer)
    Authority = db.Column(db.Integer)
    Admin = db.Column(db.Integer)
    Third_party = db.Column(db.Integer)
    Total_Real= db.Column(db.Integer)
    Total_upload = db.Column(db.Integer)
    Total_request = db.Column(db.Integer)

    def __init__(self,id,Ordinary,Authority,Admin,Third_party,Total_Real,Total_upload,Total_request):
        self.id = id
        self.Ordinary = Ordinary
        self.Authority = Authority
        self.Admin = Admin
        self.Third_party = Third_party
        self.Total_Real = Total_Real
        self.Total_upload = Total_upload
        self.Total_request = Total_request
        
#end

#INdex page

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

                other = Other(admin_approval = 'no', admin_id = '', no_of_video_upload = 0, no_of_video_request = 0, 
                third_party_issue_id = '',third_party_pending_order = '',third_party_response = '', date = '', 
                start_time = '', end_time = '', live_recording_no = 0,usr_name = username )
                db.session.add(other)
                
                value = Count.query.filter_by(id = 1).first()
                value.Ordinary = value.Ordinary + 1
                db.session.add(value)

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

                other = Other(admin_approval = 'no', admin_id = '', no_of_video_upload = 0, no_of_video_request = 0, 
                third_party_issue_id = '',third_party_pending_order = '',third_party_response = '', date = '', 
                start_time = '', end_time = '', live_recording_no = 0, usr_name = username )
                db.session.add(other)
                
                value = Count.query.filter_by(id = 1).first()
                value.Authority = value.Authority + 1
                db.session.add(value)
                
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
        session.permanent = True       
        uname = request.form['uname']
        passw = request.form['psw']
        
        login = User.query.filter_by(username=uname, password=passw).first()

        if login:
            
            if login.type == 'Admin':
                session["admin"] = uname

                return redirect(url_for('admindashboard'))

            elif login.type == 'Ordinary' or login.type == 'Authority':
                session["user"] = uname

                return redirect(url_for('current'))

            elif login.type == 'Third_party':
                session["third"] = uname
                return redirect(url_for('thirddashboard'))
            else: 
                return "ll"
        else:
            flash('User is Not Registerd','error')
            return render_template('index.html',scroll='relogin')

            
@app.route("/logout")
def logout():
    for key in session.keys():
        session.pop(key)
    return render_template('index.html',scroll='relogin')


@app.route('/')
def index():
    #return '<html><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><center><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><h1>Please Confirm Your Email Address</h1></div><div class="card-body"><br><p class="card-text">We have sent an email with a confirmation link to your email address. In order to complete the sign-up process, please click the confirmation link.<br><br>If you do not receive a confirmation email, please check your spam folder. Also, please verify that you entered a valid email address in our sign-up form.</p><br><br></div> </div><br><br><div class="card text-white bg-info" style="max-width: 80em;"><div class="card-header"><br><h4>Your Documents are sent to admin for Verification.After verification your account will be activated.<BR> Please wait for the account activation mail</h4></p><br><br></div></html>'
    return render_template('index.html')









#admin page

@app.route('/Admin')
def  admindashboard():
    if "admin" in session:
        user = session["admin"]
        return render_template('dashboard.html',user=user)
    else:
        flash('Not Allowed Please Register','error')
        return render_template('index.html',scroll='relogin')
    


@app.route('/Admin/user')
def user():
    if "admin" in session:
        user = session["admin"]
        ordinary = (db.session.query(Ordinary).filter(Ordinary.usr_name == Other.usr_name).join(Other,Other.admin_approval == 'no')).all()
        authority = (db.session.query(Authority).filter(Authority.usr_name == Other.usr_name).join(Other,Other.admin_approval == 'no')).all()
        return render_template('user.html',ordinary = ordinary,authority = authority,user=user)
    else:
        return render_template('index.html',scroll='relogin')


@app.route('/user')
def user1():
    if "admin" in session:
        user = session["admin"]
        ordinary = (db.session.query(Ordinary).filter(Ordinary.usr_name == Other.usr_name).join(Other,Other.admin_approval == 'no')).all()
        authority = (db.session.query(Authority).filter(Authority.usr_name == Other.usr_name).join(Other,Other.admin_approval == 'no')).all()
        return render_template('user.html',ordinary = ordinary,authority = authority,user=user)
    else:
        render_template('index.html',scroll='relogin')


@app.route('/Admin/user/verify/<path:username>/<path:value>')
def verify(username,value):
    if "admin" in session:
        user = session["admin"]
        print(username)
        result = value
        print(result)
        verify = Other.query.filter_by(usr_name = username).first()
        if result == 'accept':
            verify.admin_approval = 'accept'
            verify.admin_id = 'Surej'
            db.session.add(verify)
            db.session.commit()
            flash('Verified successfully')
            return redirect(url_for('user',user=user))
        elif result == 'reject':
            verify.admin_approval = 'reject'
            verify.admin_id = 'Surej'
            db.session.add(verify)
            db.session.commit()
         
            flash('Verified successfully')
            return redirect(url_for('user',user=user))
    else:
        return render_template('index.html',scroll='relogin')


         
         
@app.route('/Admin/process')
def  process():
    if "admin" in session:
        user = session["admin"]
        succ = Other.query.filter_by(third_party_pending_order ='yes' ).all()
        fail = Other.query.filter_by(third_party_pending_order ='reject' ).all()
        print(succ)
        print(fail)
        return render_template('process.html',succ = succ,fail = fail ,user=user)
    else:
        return render_template('index.html',scroll='relogin')

    

@app.route('/ID_Proof/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    if "user" in session:
        user = session["admin"]
        return send_from_directory(directory='ID_Proof', filename=filename,user=user)
    else:
        return render_template('index.html',scroll='relogin')



@app.route('/Admin/third_party', methods=["GET","POST"])
def third():
    if "admin" in session:
        user = session["admin"]
        all = db.session.query(Third.dept.distinct()).all()
        len1 = len(all)
     
     
        if request.method == "POST":
            dept = request.form['firstList']
            new = request.form['secondList']
            name = request.form['thirdList']
            phone = request.form['phone']
            mail1 = request.form['fourthList']
            if dept == 'Other':
                dept = new
            exists = Third.query.filter_by(mail = mail1).first()

            if not exists:
            
                v1 = randint(0, 1000)
                v2 = randint(0, 1000)
                value = Count.query.filter_by(id = 1).first()
                uname = dept + '_' + str(value.Third_party+1)
                third_party_id = uname
                psw=str(v1)+name+str(v2)
            

                user = User(username=uname,password=psw,type='Third_party')
                register = Third(usr_name = uname, dept=dept, name=name, mail = mail1, phone=phone, third_party_id = third_party_id)
                count = Count.query.filter_by(id = 1).first()
                count.Third_party = count.Third_party + 1
                db.session.add(user)
                db.session.add(register)
                db.session.add(count)
                db.session.commit()
            
                msg = Message('Welcome to Pinpoint Family', sender = 'pinpoint.four.2020@gmail.com', recipients = [mail1])
                msg.html = '<h5>Hi,</h5><h3>You are addded as Third Party at PINPOINT.<br>Please login PINPOINT using following details</h3><h5> Your Username : {} <br> Password : {}<br><br> Happy to connect with u <BR> Thank you<h5>'.format(uname,psw)

                mail.send(msg)


            
                flash('A new Third Party added successfully','success')
                return render_template('add_third.html',all = all, user=user)
            else:
                flash('Already Registered','error')


        if all != None:
            return render_template('add_third.html',all = all,user=user)
        else:
            return render_template('add_third.html',user=user)
    else:
        return render_template('index.html',scroll='relogin')








@app.route('/Admin/add_admin', methods=["GET","POST"])

def register():
    if "admin" in session:
        user = session["admin"]       
        if request.method == "POST":
            uname = request.form['uname']
            email = request.form['mail']
            fname = request.form['fname']
            lname = request.form['lname']
            phone = request.form['phone']

            exists = User.query.filter_by(username = uname).first()

            if not exists:
                
                v1 = randint(0, 1000)
                v2 = randint(100, 999)
                psw=str(v1)+uname+str(v2)
                value = Count.query.filter_by(id = 1).first()
                admin_id = "Admin_" + str(value.Admin+1)

                user = User(username=uname,password=psw,type='Admin')
                register = Admin(usr_name = uname,fname=fname,lname=lname,mail = email, phone=phone, admin_id = admin_id)
                count = Count.query.filter_by(id = 1).first()
                count.Admin = count.Admin + 1
                db.session.add(user)
                db.session.add(register)
                db.session.add(count)
                db.session.commit()
                
                
                msg = Message('Welcome to Pinpoint Family', sender = 'pinpoint.four.2020@gmail.com', recipients = [email])
                msg.html = '<h5>Hi {}&emsp;{},</h5><h3>You are addded as admin at PINPOINT.<br>Please login PINPOINT using following details</h3><h5> Your Username : {} <br> Password : {}<br><br> Happy to connect with u <BR> Thank you<h5>'.format(fname,lname,uname,psw)

                mail.send(msg)

                
                flash('A new admin added successfullly','success')
                return render_template('add_admin.html',user=user)
            else:
                flash('Username already taken,try somethig else','error')

            
        return render_template('add_admin.html',user=user)
    else:
        return render_template('index.html',scroll='relogin')

@app.route('/Admin/remove_user')
def remove():
    if "admin" in session:
        user = session["admin"]

        admin = Admin.query.all()
        normal= Ordinary.query.all()
        third = Third.query.all()
        officials = Authority.query.all()
        
        
        return render_template('remove.html', admin=admin,normal=normal,third=third, officials=officials,user=user)
    else:
        return render_template('index.html',scroll='relogin')



@app.route('/delete/<string:usr_name>/', methods = ['GET', 'POST'])
def delete(usr_name):
    if "admin" in session:
        user = session["admin"]
        user= User.query.filter(User.username == usr_name).first()
        print(usr_name)
        print(user.type)

        
        mydata = db.session.query(Admin).filter(Admin.usr_name == usr_name).first()

        my_data2=Ordinary.query.filter(usr_name==usr_name).first()

        my_data3=Third.query.filter(usr_name==usr_name).first()

        my_data4 = Authority.query.filter(usr_name==usr_name).first()
        count = Count.query.filter_by(id = 1).first()
        


        if user.type == "Admin":
            count.Admin = count.Admin - 1
            db.session.add(count)
            db.session.delete(mydata)
            db.session.delete(user)

        elif user.type == "Ordinary":
            count.Ordinary = count.Ordinary - 1
            db.session.add(count)
            db.session.delete(my_data2)
            db.session.delete(user)

        elif user.type == "Third_party":
            count.Third_party = count.Third_party - 1
            db.session.add(count)
            db.session.delete(my_data3)
            db.session.delete(user)

        elif user.type == "Authority":
            count.Authority = count.Authority - 1
            db.session.add(count)
            db.session.delete(my_data4)
            db.session.delete(user)

        db.session.commit()
        flash("User Deleted Successfully",'success')
        return redirect(url_for('remove',user=user))
    else:
        return render_template('index.html',scroll='relogin')



if(__name__ == "__main__"):
    app.run(debug=True)


#insert into Count(id,Ordinary,Authority,Admin,Third_party,Total_Real,Total_upload,Total_request) values (1,0,0,0,0,0,0,0);


