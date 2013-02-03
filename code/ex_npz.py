import numpy as np

a = np.linspace(0, 100, 1e7)
sina = np.sin(a)
np.savez('test.npz', a=a, sina=sina)

