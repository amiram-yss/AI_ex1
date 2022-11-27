import collections
import random
from collections import namedtuple

import numpy
import stats

import csv

NUM_OF_NAVS = 100
UP_DEPTH_LIMIT = 5
DN_DEPTH_LIMIT = 50

if __name__ == '__main__':
    junctions = stats.load_map_from_csv()
    info = stats.map_statistics(junctions)
    NUM_OF_JUNCS = info['Number of junctions']

    nav_dict = [] #numpy.array()

    for path in range(NUM_OF_NAVS):
        start_idx = random.randrange(NUM_OF_JUNCS)
        start = junctions[start_idx]
        ptr_idx = start_idx
        ptr = start
        steps = random.randrange(UP_DEPTH_LIMIT, DN_DEPTH_LIMIT)
        nxt_idx = 0
        for step in range(steps):
            links = ptr.links
            # print(len(links), " : ", links)
            nxt_idx = random.randrange(len(links))
            # print("Next idx: ", nxt_idx)
            ptr = junctions[links[nxt_idx].target]
            # print(ptr)
        '''if len(ptr.links) == 0:
            print("SKIP")
            continue'''
        if len(ptr.links) == 0:
            nav_dict.append((start_idx, ptr.index))
            break
        nav_dict.append((start_idx, ptr.links[0].target))
    # print(len(nav_dict), " : ", nav_dict)
    file = open('problems.csv', 'w', newline='')
    writer = csv.writer(file)
    for itr in nav_dict:
        print(itr)
        writer.writerow(itr)
    file.close()
