import collections
import random
from collections import namedtuple

import numpy
import stats

NUM_OF_NAVS = 100
UP_DEPTH_LIMIT = 5
DN_DEPTH_LIMIT = 20

if __name__ == '__main__':
    junctions = stats.load_map_from_csv()
    info = stats.map_statistics(junctions)
    NUM_OF_JUNCS = info['Number of junctions']

    for path in range(1): #range(NUM_OF_NAVS):
        start = random.randrange(NUM_OF_JUNCS)
        ptr = start
        steps = random.randrange(UP_DEPTH_LIMIT, DN_DEPTH_LIMIT)
        for step in range(steps):
            nxt_idx =