import numpy as np

data = np.arange(1e7)
np.save('test.npy', data)
data2 = np.load('test.npy')

assert np.alltrue(data == data2)
