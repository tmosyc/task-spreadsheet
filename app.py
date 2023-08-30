from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from spreed_sheet import insert
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")

db.init_app(app)

@app.route("/",methods=['GET'])
def index():
    datas = task_data.query.all()
    return render_template('index.html', datas = datas)
    
@app.route("/task_register",methods=['POST'])
def task_register():
    task_title = request.form.get('task_title')
    task_content = request.form.get('task_content')
    tasks = task_data(title=task_title, content = task_content)
    db.session.add(tasks)
    db.session.commit()
    
    insert(task_title,task_content)
    
    return redirect("/")

@app.route("/delete/<task_id>",methods=['POST'])
def task_delete(task_id):
    task = task_data.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect("/")


class task_data(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)

with app.app_context():
    db.create_all()
    