import sys
sys.path.append('..')
from tetra3 import Tetra3, get_centroids_from_image
from PIL import Image
from pathlib import Path
from astropy.io import fits


fields = [1, 2, 3, 4, 5, 6, 7, 8]


for field in fields:
    t3 = Tetra3('gaia{}_database'.format(field))

    path = Path('/home/aleks/astrom/')
    for impath in path.glob('{}-*.fit'.format(field)):
        print('Solving for image at: ' + str(impath))
        with fits.open(impath) as hdu:
            img = Image.fromarray(hdu[0].data)
            centroids = get_centroids_from_image(hdu[0].data)
            result = t3.solve_from_centroids(centroids, size=img.size, fov_estimate=0.4)
            print(result)
