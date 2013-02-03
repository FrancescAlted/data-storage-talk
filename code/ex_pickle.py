import pickle

filename, colors = '/tmp/ex_pickle', ['red', 'black']

with open(filename, 'wb') as f:
    pickle.dump(colors, f)

# ... later on
with open(filename, 'rb') as f:
    obj = pickle.load(f)

assert colors == obj
