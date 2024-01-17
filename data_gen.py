# DOWNLOAD `entity_vector.model.bin` FROM https://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/

import pickle
import re

import gensim
import numpy as np
from tqdm import tqdm

model = gensim.models.KeyedVectors.load_word2vec_format('./entity_vector.model.bin', binary=True)


def is_katakana(s):
    return re.match(r'^[\u30A0-\u30FF]+$', s)


index_to_word = {}
for word, index in tqdm(model.key_to_index.items()):
    word = word.strip('[]')
    if not is_katakana(word):
        continue
    if not (3 <= len(word) <= 6):
        continue
    index_to_word[index] = word

index_vec = np.array(list(index_to_word.keys()))
index_vec.sort()
words = [index_to_word[idx] for idx in index_vec]
vectors = model.vectors[index_vec].astype(np.float16)

data = dict(
    words=words,
    vectors=vectors
)

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# print(model.most_similar(positive=['ディープ']))
# print(model.most_similar(positive=['インパクト']))
