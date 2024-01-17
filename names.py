import codecs
import pickle
import re
from pprint import pprint

import bs4

with codecs.open('names.html', 'r', 'utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), features='lxml')


def is_katakana(s):
    return re.match(r'^[\u30A0-\u30FF]+$', s)


names = set()

for a in soup.select('li > a'):
    if 'href' not in a.attrs:
        continue
    if not a.attrs['href'].startswith(r'/wiki/'):
        continue
    if not is_katakana(a.text):
        continue
    names.add(a.text)

# print(names)

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

words = data['words']

word_set = set(words)


def split_name(source):
    for i in range(1, len(source) - 1):
        a, b = source[:i], source[i:]
        if a in word_set and b in word_set:
            yield a, b


name_parts = []

for name in names:
    splits = list(split_name(name))
    # print(name, splits)

    if not splits:
        continue

    pair, *_ = splits
    name_parts.append(pair)

# pprint(name_pairs)
