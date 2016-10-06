################
# Twittercroft #
################

Technical Exercise by Verisk Maplecroft as completed by Mikuláš Mrva.

Build a simple web based web application which:
 
* Displays the latest 10 tweets from Maplecroft's Twitter feed
* Displays an interactive map of the tweets where it’s possible to associate the tweet with a country or other location.
 

# Installation guide (on Linux)

1. Download the code

    * `git clone https://github.com/mikulas-mrva/twittercroft`

2. Start a new virtual environment with Python 3.5

    * `cd twittercroft`
    
    * `virtualenv env --python=python3`
    
    * `. env/bin/activate`

3. Install required packages

    * `pip install -r requirements.txt`

4. Migrate DB

    * `./manage.py migrate`

5. Import list of countries

    * `./manage.py import_countries data/countries.csv`

6. Enter your Twitter App credentials

    * `nano twittercroft/local_settings.py`
        
    * ```
        # Uncomment this if you want to run this with a debug server:
        # DEBUG = True
        # otherwise, uncomment and set this:
        # ALLOWED_HOSTS = []
    
        TWITTER_API_CONSUMER_KEY = 'your-consumer-key'
        TWITTER_API_CONSUMER_SECRET = 'your-secret-key'
        TWITTER_API_ACCESS_TOKEN = 'your-access-token'
        TWITTER_API_ACCESS_SECRET = 'your-access-secret'
    
        # uncomment and edit this if you want to access another user's tweets:
        # TWITTER_MAPLECROFT_USER_ID = 'maplecroftrisk' 
        ```
