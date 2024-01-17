import codecs
import pickle

import gensim
import numpy as np

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


n = 256
name_parts_idx = np.arange(len(name_parts))
generated_names = []
for _ in range(n):
    name_elements = name_parts[np.random.choice(name_parts_idx)]
    name = ' '.join(choose_similar(elm) for elm in name_elements)
    name = name.replace('・', '')
    generated_names.append(name)
    print(name)

with codecs.open('out.txt', 'w', 'utf-8') as f:
    f.write('\n'.join(generated_names))

# print(model.most_similar(positive=['ディープ']))
# print(model.most_similar(positive=['インパクト']))
