import requests


# TODO: Read all built-in functions of python 3.5
def read_document():
    with open('movie_quotes.txt', 'r') as f:
        text = f.read()
        return text


def is_contains_curse_word(quotes):
    # url_api = "http://www.purgomalum.com/service/containsprofanity?text={}".format(quotes)
    url_api = "http://www.wdylike.appspot.com/?q={}".format(quotes)
    r = requests.get(url_api)
    if r.text == 'true':
        return True
    return False


if __name__ == '__main__':
    quotes = read_document()
    if is_contains_curse_word(quotes):
        print("This paragraph is containing curse words!")
    else:
        print("Okay, polite enough!")
