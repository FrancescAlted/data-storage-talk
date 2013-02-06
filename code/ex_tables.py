import tables
import numpy as np

f = tables.openFile("example.h5", "w")
group = f.createGroup("/", "reduced_data")
ds = f.createArray(group, "array", np.array([1, 2, 3, 4]))

gen = ((i, i*2, i**3) for i in xrange(1000000))
sa = np.fromiter(gen, dtype="i4,i8,f8")
tab = f.createTable(f.root, 'table', sa)
