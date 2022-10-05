from json import load as json_load, dumps as json_dumps
from twitter_api import init_twitter_api
from random import choice as random_quote


def main():

    # init access to the twiter account
    twitter = init_twitter_api()

   # parsing json data file
    with open("data/quotes.json") as json_file:
        data = json_load(json_file)

    quote = find_quote(data)

    print(f'"{quote["Quote"]}" \n \n - {quote["Author"]}')
    # line that actually creates the tweet, commented out for now
    # twitter.update_status(quote["Quote"])


def find_quote(data):

    while True:
        quote = random_quote(data)

        if len(quote["Quote"]) < 280 and not quote_used(quote):
            break

    set_quote_used(quote)

    return quote


def quote_used(quote):
    used_quote = json_dumps(quote)
    pass


def set_quote_used(quote):
    # adds quote to list of used quotes(json file), to be implemented
    pass


if __name__ == "__main__":
    main()
