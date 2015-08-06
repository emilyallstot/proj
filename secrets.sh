# Secrets for Yelp API v2.0
#
# This file should never go into github!

export YELP_CONSUMER_KEY="R080nr_hRZcH3zNCpwksoA"
export YELP_CONSUMER_SECRET="Pn3bflZgqDP-TzW6iR3tTYx9M5k"
export YELP_ACCESS_TOKEN="4yZl1-2cVlG_iSL9-C7hbR45P05wxquc"
export YELP_ACCESS_TOKEN_SECRET="JmUZo0HUzLHYSVQp2Wm2w4PGbKs"

export TWITTER_CONSUMER_KEY="vh1ge2fOb7ngGIBgnRzlK1q8k"
export TWITTER_CONSUMER_SECRET="WXGW6OyC0DSmlMOdECYcUCHsfIldGTx2Z4BGq5sBJ3DSZtgV7M"
export TWITTER_ACCESS_TOKEN_KEY="3306309254-tJRsusgIvKJZov2C5RCFuRNihMx8bzT5CXG2Esn"
export TWITTER_ACCESS_TOKEN_SECRET="NgSjIxbnXHL9M3M2kNJF8lSKvNd9q5aWY7NHHf1GRERaU"

# http://blueprintinteractive.com/tutorials/instagram/uri.php?code=80de9f1ff2634b6db400421ce119e993
export INSTAGRAM_ACCESS_TOKEN="2074318629.1fb234f.1730e31b95984bb9844c7138de02eacb"
export INSTAGRAM_CLIENT_SECRET="ef87d418362745b9a4a5c6c2718ec43a"
export INSTAGRAM_CLIENT_ID="1233e76656384c689cb0bbd54a28c47a"



# https://instagram.com/oauth/authorize/?client_id=1233e76656384c689cb0bbd54a28c47a&redirect_uri=http://localhost&response_type=token

# 7e2ab48a50844dd18f6166e723533f83

# https://instagram.com/oauth/authorize/?client_id=266815079b09429c938707621f69f273&redirect_uri=http://localhost:5000&response_type=token&scope=likes+comments+relationships+basic

# 2074318629.2668150.516ce003bc214373b133442f2132af41
# # {"access_token":"2074318629.2668150.516ce003bc214373b133442f2132af41","user":{"username":"manimapsf","bio":"Map of nail salons in San Francisco - coming soon!","website":"http:\/\/ManiMapSF.com","profile_picture":"https:\/\/instagramimages-a.akamaihd.net\/profiles\/anonymousUser.jpg","full_name":"","id":"2074318629"}}(env)user@nuc03:~/Desktop/ManiMapSF$ 



# Visit this page and authorize access in your browser: 
# https://instagram.com/accounts/login/?force_classic_login=&next=/oauth/authorize%3Fscope%3Dbasic%26redirect_uri%3Dhttp%3A//localhost%3A5000/instagram_callback%26response_type%3Dcode%26client_id%3D266815079b09429c938707621f69f273
# Paste in code in query string after redirect: 7e2ab48a50844dd18f6166e723533f83
# access token: 
# (u'2074318629.2668150.516ce003bc214373b133442f2132af41', 
    # {u'username': u'manimapsf', 
    # u'bio': u'Map of nail salons in San Francisco - coming soon!', 
    # u'website': u'http://ManiMapSF.com', 
    # u'profile_picture': u'https://instagramimages-a.akamaihd.net/profiles/anonymousUser.jpg', 
    # u'full_name': u'', 
    # u'id': u'2074318629'})

# access token: 
# (u'2074318629.2668150.516ce003bc214373b133442f2132af41', {u'username': u'manimapsf', u'bio': u'Map of nail salons in San Francisco - coming soon!', u'website': u'http://ManiMapSF.com', u'profile_picture': u'https://instagramimages-a.akamaihd.net/profiles/anonymousUser.jpg', u'full_name': u'', u'id': u'2074318629'})

# curl -F 'client_id=266815079b09429c938707621f69f273' \
#     -F 'client_secret=0e23e8eee81d47428e813c94e4d060d4' \
#     -F 'grant_type=authorization_code' \
#     -F 'redirect_uri=http://localhost:5000' \
#     -F 'code=5e1369b5dec3447298d92f4b41ad3c2f' \
#     https://api.instagram.com/oauth/access_token

#     https://api.instagram.com/oauth/authorize/?client_id=266815079b09429c938707621f69f273&redirect_uri=http://localhost:5000&response_type=code