import re
import json
from datetime import datetime

def days():
    most_days = {}
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweet = json.loads(line)
        date_tweet = datetime.fromisoformat(tweet["date"]).strftime('%m/%d/%Y')
        if date_tweet in most_days.keys():
            most_days[date_tweet] += 1
        else:
            most_days[date_tweet] = 1
    lista_most_days = sorted(most_days.items(), key=lambda x: x[1], reverse=True)
    top_10 = lista_most_days[0:10]
    return top_10

        
