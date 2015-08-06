"""Data model for businesses."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Business(db.Model):
    """Map points for bears."""

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

        return "<Business business_id=%s yelp_id=%s>" % (self.business_id, self.yelp_id)


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nailsalons.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
