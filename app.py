from flask import Flask, render_template, redirect
import pymongo
import sys
#from flask_pymongo import PyMongo
import scrape_to_mars
from pymongo import MongoClient


#Open Flask
app = Flask(__name__)

#Connect to mongodb
conn = "mongodb://localhost:27017"
mongo_mars = pymongo.MongoClient(conn)

#mongo_mars = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mongo_mars"
#mongo_mars = PyMongo(app)


@app.route("/")
def index():
   
    mars_data=mongo_mars.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():
    mars_data_b=mongo_mars.db.mars_data
    mars_scrp=scrape_to_mars.scrp_mars_news()
    mars_scrp=scrape_to_mars.scrp_mars_image()
    mars_scrp=scrape_to_mars.scrp_mars_wthr()
    mars_scrp=scrape_to_mars.scrp_mars_facts()
    mars_scrp=scrape_to_mars.scrp_mars_hemi()
    mars_data_b.update({}, mars_scrp, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True) 


