import json
from twitter_api import init_twitter_api
import random


def main():

    # init access to the twiter account
    api = init_twitter_api()

   # parsing json data file
    with open("data/quotes.json") as json_file:
        data = json.load(json_file)

    quote = find_quote(data)

    print(quote["Quote"])
    # line that actually creates the tweet, commented out for now
    # api.update_status(quote["Quote"])


def find_quote(data):

    while True:
        quote = random.choice(data)

        if len(quote["Quote"]) < 280 and not quote_used(quote):
            break

    set_quote_used(quote)

    return quote


def quote_used(quote):
    # checks if quote has already been used, to be implemented
    pass


def set_quote_used():
    # adds quote to list of used quotes(json file), to be implemented
    pass


if __name__ == "__main__":
    main()
