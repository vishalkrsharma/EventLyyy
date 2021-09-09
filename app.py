from flask import Flask,redirect,render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class form1(db.Model):
    # only for test purpose that is used for import
    sno = db.Column(db.Integer, primary_key = True)
    rollnumber = db.Column(db.Integer, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    # it is only use for export
    def _repr_(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/' , methods = ["GET","POST"])
def home():
     if request.method == 'POST':
         rollnumber = request.form['rollnumber']
         password = request.form['password']

         # data automatically going in the sql server
         form1 = form1(rollnumber = rollnumber, password = password)
         db.session.add(form1)
         db.session.commit()
         form1 = form1.query.all()
         print(form1)

         return render_template('thank.html')
     return render_template('index.html')



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)