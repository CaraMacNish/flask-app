from flask import Flask
#from config import Config
#from flask_pymongo import PyMongo
from flask import render_template, flash, redirect, url_for
from pymongo import MongoClient
client = MongoClient("mongodb+srv://cara:gumpt10n@cluster0.gbmri.mongodb.net/workout?retryWrites=true&w=majority")
#db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#print(serverStatusResult)

db = client.workout
count = db.members.count_documents({})
          
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', count = count)
#    return render_template('index.html')
