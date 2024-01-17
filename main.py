import gensim
from pprint import pprint
import re
import numpy as np
import pickle
from tqdm import tqdm
from names import name_parts

# data = dict(
#     words=words,
#     vectors=vectors
# )

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

words, vectors = data['words'], data['vectors']

model = gensim.models.KeyedVectors(vector_size=vectors.shape[1])
model.add_vectors(words, vectors)


def choose_similar(source):
    candidates = model.most_similar(source, topn=16)
    odds = np.array([p for _, p in candidates])
    odds /= odds.sum()
    odds **= 20
    odds /= odds.sum()
    i, = np.random.choice(np.arange(len(candidates)), size=1, p=odds)
    return candidates[i][0]


n = 16
name_parts_idx = np.arange(len(name_parts))
for _ in range(n):
    name_elements = name_parts[np.random.choice(name_parts_idx)]
    name = ' '.join(choose_similar(elm) for elm in name_elements)
    name = name.replace('・', '')
    print(name.replace('・', ''))

# print(model.most_similar(positive=['ディープ']))
# print(model.most_similar(positive=['インパクト']))
