from retweeted import retweeted

def main():
    """ Main program """
    option = input('Please select an option: \n'
                   '(1) Top 10 tweets más retweeted \n'  
                   '(2) Top 10 usarios con más tweets \n'  
                   '(3) Top 10 de días con más tweets \n'
                   '(4) Top 10 de hashtags más usados \n')
    if option == '1':
        retweeted()
    return 0

if __name__ == "__main__":
    main()