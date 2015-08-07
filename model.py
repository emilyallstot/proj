"""Data model for businesses."""

from flask_sqlalchemy import SQLAlchemy
import sqlite3
import phonenumbers


db = SQLAlchemy()


class Business(db.Model):
    """Map points and yelp details for businesses."""

    __tablename__ = "businesses"

    business_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    business_name = db.Column(db.String(64))
    yelp_id = db.Column(db.String(64))
    bus_lat = db.Column(db.String(32))
    bus_long = db.Column(db.String(32))
    address = db.Column(db.String(64))
    phone = db.Column(db.String(32))


    def __repr__(self):
        """Pretty printing"""

        return "<Business business_name=%s yelp_id=%s>" % (self.business_name, self.yelp_id)

    @classmethod
    def get_by_id(cls, business_id):
        """Query for a specific business in the database by the primary key"""

        cursor = db_connect()
        QUERY = """
                  SELECT *
                   FROM Businesses
                   WHERE business_id = ?;
               """

        cursor.execute(QUERY, (business_id,))

        row = cursor.fetchone()
        
        if not row:
            return None

        business = Business()
        business.business_id = row[0]
        business.business_name = row[1]
        business.yelp_id = row[2]
        business.bus_lat = row[3]
        business.bus_long = row[4]
        business.address = row[5]
        business.phone = row[6]

        return business

class Infos(db.Model):
    """Additional information about businesses from other sources."""

    __tablename__ = "infos"

    yelp_id = db.Column(db.String(64), primary_key=True)
    website_url = db.Column(db.String(128))
    yelp_url = db.Column(db.String(128))
    facebook_url = db.Column(db.String(128))
    instagram_url = db.Column(db.String(128))
    twitter_url = db.Column(db.String(128))
    emily_url = db.Column(db.String(128))

    def __repr__(self):
        """Pretty printing"""

        return "<Infos yelp_id=%s>" % (self.yelp_id)

    @classmethod
    def get_by_yelp_id(cls, yelp_id):
        """Query for a specific business in the database by the primary key"""

        cursor = db_connect()
        QUERY = """
                  SELECT *
                   FROM Infos
                   WHERE yelp_id = ?;
               """

        cursor.execute(QUERY, (yelp_id,))

        row = cursor.fetchone()
        
        if not row:
            return None

        info = Infos()
        info.yelp_id = row[0]
        info.website_url = row[1]
        info.yelp_url = row[2]
        info.facebook_url = row[3]
        info.instagram_url = row[4]
        info.twitter_url = row[5]
        info.emily_url = row[6]

        return info




##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///businesses.db'
    db.app = app
    db.init_app(app)

def db_connect():
    """Return a database cursor."""

    conn = sqlite3.connect("businesses.db")
    cursor = conn.cursor()
    return cursor

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."