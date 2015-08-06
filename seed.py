"""Load business data into database."""

from model import Business, connect_to_db, db
from server import app


def get_businesses():
    """Load businesses from dataset into database."""

    for i, row in enumerate(open('data/yelp_data.csv')):
        row = row.rstrip()
        business_name, yelp_id, bus_lat, bus_long, address, phone = row.split("|")

        business = Business(business_name=business_name,
                    yelp_id=yelp_id,
                    bus_lat=bus_lat,
                    bus_long=bus_long,
                    address=address,
                    phone=phone)

        db.session.add(business)

        if i % 100 == 0:
            print i

    db.session.commit()


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()
    get_businesses()

