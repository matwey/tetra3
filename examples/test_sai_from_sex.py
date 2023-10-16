import sys
sys.path.append('..')
from tetra3 import Tetra3, get_centroids_from_image
from pathlib import Path
from astropy.io import fits
import pandas as pd
import numpy as np

fields = [1, 2, 3, 4, 5, 6, 7, 8]
size = (2048, 2048)

for field in fields:
    t3 = Tetra3('gaia{}_database'.format(field))

    path = Path('/home/aleks/astrom/')
    for catpath in path.glob('{}-*.icat'.format(field)):
        print('Solving for catalog at: ' + str(catpath))
        x = pd.read_table(catpath, sep="\s+", header=None, names=["number", "flux", "fluxerr", "mag", "magerr", "x", "y", "flags", "fwhm"], index_col=0, comment="#")
        order = np.argsort(np.asarray(x["flux"]))[::-1]
        centroids = np.column_stack([x["x"], x["y"]])[order]
        result = t3.solve_from_centroids(centroids, size=size, fov_estimate=0.4)
        print(result)
