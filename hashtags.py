import re
import json

def hashtag():
    most_hashtags = {}
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweet = json.loads(line)
        txt = tweet["content"]
        cantidad = len(re.findall("#", txt))
        for i in range(0, cantidad):
            x = re.search("#", txt)
            if x:
                inicio = x.start()
            else:
                break
            txt2 = txt[int(inicio):]
            if re.search(" ", txt2) and re.search("\n", txt2):
                n = re.search("\n", txt2).start()
                space = re.search(" ", txt2).start()
                if space < n:
                    fin = space
                else:
                    fin = n
            elif re.search(" ", txt2):
                fin = re.search(" ", txt2).start()
            
            elif re.search("\n", txt2):
                fin = re.search("\n", txt2).start()
            else:
                fin = len(txt)-inicio

            if txt[inicio:inicio+fin][-1] == "." or txt[inicio:inicio+fin][-1] == ",":
                fin -= 1
            hashtag = txt[inicio:inicio+fin]
            txt = txt[inicio+fin:]
            if  hashtag in most_hashtags.keys():
                most_hashtags[hashtag] += 1
            else:
                most_hashtags[hashtag] = 1
    lista_most_hashtags = sorted(most_hashtags.items(), key=lambda x: x[1], reverse=True)
    top_10 = lista_most_hashtags[0:10]
    return top_10