"""Load business data into database."""

from model import Business, Infos, connect_to_db, db
from server import app
import phonenumbers


def get_businesses():
    """Load businesses from Business dataset into database."""

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


def get_infos():
    """Load infos from Infos dataset into database."""

    for i, row in enumerate(open('data/info_data.csv')):
        row = row.rstrip()

        yelp_id, website_url, yelp_url, facebook_url, instagram_url,\
        twitter_url, emily_url = row.split("|")

        infos = Infos(yelp_id=yelp_id,
                    website_url=website_url,
                    yelp_url=yelp_url,
                    facebook_url=facebook_url,
                    instagram_url=instagram_url,
                    twitter_url=twitter_url,
                    emily_url=emily_url)
        db.session.add(infos)

        if i % 100 == 0:
            print i

    db.session.commit()



if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()
    get_infos()
    get_businesses()

