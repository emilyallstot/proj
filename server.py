"""Demonstration of Google Maps."""

from flask import Flask, render_template, jsonify, redirect, flash, session
import jinja2
from model import connect_to_db, Business, Infos
import os
import yelp
import csv
import phonenumbers


app = Flask(__name__)
app.secret_key = "ursusmaritimus"



# YELP STUFF BELOW

yelp_api = yelp.Api(
    consumer_key=os.environ['YELP_CONSUMER_KEY'],
    consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
    access_token_key=os.environ['YELP_ACCESS_TOKEN'],
    access_token_secret=os.environ['YELP_ACCESS_TOKEN_SECRET'])

def address_formatted(raw_address):
    address_string = ""
    for line in raw_address:
        address_string = address_string + line + ' '
    return address_string

def phone_formatted(raw_phone):
    phone_string = ""
    if raw_phone:
        phone_string = phonenumbers.parse(raw_phone, "US")
        phone_string = phonenumbers.format_number(phone_string, phonenumbers.PhoneNumberFormat.NATIONAL)
    return phone_string


def yelp_to_salon_list_SF(search_term, yelp_ids_dict):
    print "in this method to get salon"
    search_results = yelp_api.Search(term=search_term, limit=5, location="San Francisco, CA", radius_filter=6000, categories="beautysvc,othersalons")
    total_results = search_results.total

    offset = total_results % 20 - 1

    while offset < total_results:
        search_results_expanded = yelp_api.Search(term=search_term, offset=offset, location="San Francisco, CA", radius_filter=1200, categories="beautysvc,othersalons")
        for business in search_results_expanded.businesses:
            if business.name not in yelp_ids_dict:
                yelp_ids_dict[business.id] = { \
                'yelp_id' : business.id, \
                'business_name': business.name, \
                'bus_lat': business.location.coordinate[u'latitude'], \
                'bus_long': business.location.coordinate[u'longitude'], \
                'address': address_formatted(business.location.address), \
                'phone': phone_formatted(business.phone)}
                print yelp_ids_dict[business.id]['phone'], business.name
                print "in this method to get salon"

                
        offset = offset + 20

    return yelp_ids_dict





@app.route('/')
def map():
    """Show map of businesses."""

    return render_template("map.html")


@app.route('/businesses.json')
def business_info():
    """JSON information about businessess."""
    print "hello"
    
    yelp_ids_empty = {}
    yelp_ids_dict = yelp_to_salon_list_SF('nail salon', yelp_ids_empty)

    businesses = {}

    # for business in yelp_ids_dict:
    #     businesses = {
    #         business.yelp_id: {
    #             "yelpID": business.yelp_id,
    #             "businessName": business.business_name,
    #             "busLat": business.bus_lat,
    #             "busLong": business.bus_long,
    #             "address": business.address,
    #             "phone": business.phone
    #         }
    #     }


    return jsonify(yelp_ids_dict)



# @app.route("/salonpages/<int:business_id>")
# def show_business(business_id):
#     """Return page showing the details of a given business. 
    
#     Show all info about a business.
#     """
    
#     business = Business.get_by_id(business_id)
#     infos = Infos.get_by_yelp_id(business.yelp_id)
#     print infos

#     return render_template("business_details.html",
#                            display_business=business, display_infos=infos)




if __name__ == "__main__":
    app.config['DEBUG'] = True
    connect_to_db(app)
    app.run()






