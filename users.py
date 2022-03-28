import json
import operator


def users():
    most_users = {}
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweet = json.loads(line)
        if len(most_users) < 10:
            if tweet['user']['username'] in most_users.keys():
                if tweet['user']['statusesCount'] > most_users[tweet['user']['username']]:
                    most_users[tweet['user']['username']] = tweet['user']['statusesCount']
            else:
                most_users[tweet['user']['username']] = tweet['user']['statusesCount']
            if len(most_users) == 10:
                lista_most_users = sorted(most_users.items(), key=lambda x: x[1], reverse=True)
        else:
            if lista_most_users[9][1] < tweet['user']['statusesCount']:
                if tweet['user']['username'] in most_users.keys():
                    if tweet['user']['statusesCount'] > most_users[tweet['user']['username']]:
                        most_users[tweet['user']['username']] = tweet['user']['statusesCount']
                        lista_most_users = sorted(most_users.items(), key=lambda x: x[1], reverse=True)
                else:
                    most_users.pop(lista_most_users[9][0])
                    most_users[tweet['user']['username']] = tweet['user']['statusesCount']
                    lista_most_users = sorted(most_users.items(), key=lambda x: x[1], reverse=True)
    return lista_most_users
