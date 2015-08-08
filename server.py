"""Demonstration of Google Maps."""

from flask import Flask, render_template, jsonify, redirect, flash, session
import jinja2
from model import connect_to_db, Business, Infos


app = Flask(__name__)
app.secret_key = "ursusmaritimus"


@app.route('/')
def map():
    """Show map of businesses."""

    return render_template("map.html")


@app.route('/businesses.json')
def business_info():
    """JSON information about businessess."""

    businesses = {
        business.business_id: {
            "businessID": business.business_id,
            "businessName": business.business_name,
            "yelpID": business.yelp_id,
            "busLat": business.bus_lat,
            "busLong": business.bus_long,
            "address": business.address,
            "phone": business.phone
        }
        for business in Business.query.all()}

    return jsonify(businesses)


@app.route("/salonpages/<int:business_id>")
def show_business(business_id):
    """Return page showing the details of a given business. 
    
    Show all info about a business.
    """
    
    business = Business.get_by_id(business_id)
    infos = Infos.get_by_yelp_id(business.yelp_id)
    print infos

    return render_template("business_details.html",
                           display_business=business, display_infos=infos)




if __name__ == "__main__":
    app.config['DEBUG'] = True
    connect_to_db(app)
    app.run()
