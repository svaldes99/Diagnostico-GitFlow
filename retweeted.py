import json
import operator
 
# Opening JSON file
# f = open('farmers-protest-tweets-2021-03-5.json')
 
# returns JSON object as
# a dictionary
# data = json.load(f)

def retweeted():
    most_retweeted = []
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweet = json.loads(line)
        if len(most_retweeted) < 10:
            most_retweeted.append(tweet)
            if len(most_retweeted) == 10:
                most_retweeted.sort(key=operator.itemgetter('retweetCount'), reverse = True)
        else:
            if most_retweeted[9]['retweetCount'] < tweet['retweetCount']:
                most_retweeted[9] = tweet
                most_retweeted.sort(key=operator.itemgetter('retweetCount'), reverse = True)
    return_list = []
    for i in most_retweeted:
        return_list.append(f"{i['content']} ")
    return print(return_list)
           
 



 
# Iterating through the json
# list
 
# Closing file