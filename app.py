from flask import Flask
#from config import Config
#from flask_pymongo import PyMongo
from flask import render_template, flash, redirect, url_for
from pymongo import MongoClient

#client = MongoClient("mongodb+srv://cara:gumpt10n@cluster0.gbmri.mongodb.net/workout?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://doadmin:67043jpdw95Sq2mg@db-mongodb-nyc3-27402-613a8ebd.mongo.ondigitalocean.com/admin?authSource=admin&replicaSet=db-mongodb-nyc3-27402&tls=true&tlsCAFile=ca-certificate.crt")
#db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#print(serverStatusResult)
          
app = Flask(__name__)

db = client.workout
count = db.members.count_documents({})
#count = 4

@app.route('/')
def index():
    return render_template('index.html', count = count)
#    return render_template('index.html')
