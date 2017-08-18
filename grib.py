from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://igor:lipton@10.120.40.14:5432/igor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://igor:Lipton518@grib.cloudns.cc:5432/igor'
db = SQLAlchemy(app)


class Gusers(db.Model):
    __tablename__ = 'g_users'
    uid = db.Column('usr_id', db.INTEGER, primary_key=True)
    name = db.Column('usr_name', db.Unicode)
    pwd = db.Column('usr_pass', db.Unicode)
    email = db.Column('usr_email', db.Unicode)

    def __init__(self, uid, name, pwd, email):
        self.uid = uid
        self.name = name
        self.pwd = pwd
        self.email = email


@app.route('/')
def home():
    title = 'Тест заголовка'
    name = 'реконструкции.'
    return render_template('index.html', title=title, name=name)


@app.route('/database')
def database():
    title = 'База данных'
    return render_template('database.html', title=title, items=Gusers.query.all())


@app.route('/user/<usr_code>')
def usr_show(usr_code):
    return render_template('user.html', title='User', item=Gusers.query.filter_by(uid=usr_code).first())

if __name__ == '__main__':
    app.run(debug=True)
