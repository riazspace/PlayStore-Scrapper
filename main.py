from google_play_scraper import Sort, reviews, app
import pandas as pd
import numpy as np
import csv


app_name = 'com.nianticlabs.pokemongo'

out_file = open("pokeman.csv", 'w')
# out_file = open(app_name.split('.')[1]+".csv", 'w')
csvwriter = csv.writer(out_file)

print("Started...")
us_reviews, c_token = reviews(
    app_name,
    count=100,  # sleep_milliseconds=0, # defaults to 0
    lang='en',  # defaults to 'en'
    country='us',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
)

for i in range(0, 1000):

    us_reviews, c_token = reviews(
        app_name,
        continuation_token=c_token,

        count=100,
        # sleep_milliseconds=0, # defaults to 0
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    )
    print(i)

    for ur in us_reviews:
        csvwriter.writerow([ ur['content']])

out_file.close()



