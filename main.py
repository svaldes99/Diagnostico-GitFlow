from retweeted import retweeted
from users import users
from days import days
from hashtags import hashtag

def main():
    """ Main program """
    option = input('Please select an option: \n'
                   '(1) Top 10 tweets más retweeted \n'  
                   '(2) Top 10 usarios con más tweets \n'  
                   '(3) Top 10 de días con más tweets \n'
                   '(4) Top 10 de hashtags más usados \n')
    if option == '1':
        for i in retweeted():
            print(i +"\n")
    elif option == '2':
        for i in users():
            print(str(i[0]) + " " + str(i[1]) +"\n")
    elif option == '3':
        for i in days():
            print(str(i[0]) + " " + str(i[1]) +"\n")
    elif option == '4':
        for i in hashtag():
            print(str(i[0]) + " " + str(i[1]) +"\n")
            

if __name__ == "__main__":
    main()