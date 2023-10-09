import sys
sys.path.append('..')
from tetra3 import Tetra3


star_max_magnitude = 16


databases = {
    1 : {
        "range_ra" : (240, 250),
        "range_dec" : (30, 40),
    },
    2 : {
        "range_ra" : (265, 275),
        "range_dec" : (-20, -10),
    },
    3 : {
        "range_ra" : (225, 235),
        "range_dec" : (35, 45),
    },
    4 : {
        "range_ra" : (300, 310),
        "range_dec" : (30, 40),
    },
    5 : {
        "range_ra" : (285, 295),
        "range_dec" : (0, 10),
    },
    6 : {
        "range_ra" : (315, 325),
        "range_dec" : (40, 50),
    },
    7 : {
        "range_ra" : (330, 340),
        "range_dec" : (-5, 5),
    },
    8 : {
        "range_ra" : (345, 355),
        "range_dec" : (50, 60),
    },
}


t3 = Tetra3()

for db_num, args in databases.items():
    t3.generate_database(max_fov=0.4,
        save_as='gaia{}_database'.format(db_num),
        star_catalog='gaiadr3',
        star_max_magnitude=star_max_magnitude,
        range_ra=args["range_ra"],
        range_dec=args["range_dec"])
