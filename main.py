import json


def main():
   # parsing json file
    with open("data/quotes.json") as json_file:
        data = json.load(json_file)

    funny_quotes = find_funny_quotes(data)

    print(funny_quotes)


def find_funny_quotes(data):
    funny_quotes = list()

    for element in data:
        if "funny" in element["Tags"]:
            funny_quotes.append(element)

    return funny_quotes


if __name__ == "__main__":
    main()
