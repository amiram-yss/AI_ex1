'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple

import numpy

import stats
from ways import load_map_from_csv


def __count_links(roads):
    link_counter = 0
    for itr in roads.iterlinks():
        link_counter += 1
    return link_counter


def __link_distances(roads):
    max_dist = 0
    min_dist = numpy.Infinity
    ctr = 0
    total = 0
    for itr in roads.iterlinks():
        ctr += 1
        cur_dist = itr.distance
        total += cur_dist
        if max_dist < cur_dist:
            max_dist = cur_dist
        if min_dist > cur_dist:
            min_dist = cur_dist
    avg = total / ctr
    return max_dist, min_dist, float("{:.4f}".format(avg))


def outgoing_branching_factor_calc(roads):
    min_fact = numpy.Infinity
    max_fact = 0
    total = 0
    junc_ctr = 0
    link_per_junc_ctr = 0
    for junc_itr in roads.junctions():
        junc_ctr += 1
        for itr in junc_itr.links:
            link_per_junc_ctr += 1
        total += link_per_junc_ctr
        if link_per_junc_ctr > max_fact:
            max_fact = link_per_junc_ctr
        if link_per_junc_ctr < min_fact:
            min_fact = link_per_junc_ctr
        link_per_junc_ctr = 0
    avg = total / junc_ctr
    return max_fact, min_fact, float("{:.4f}".format(avg))


def map_statistics(roads):
    (max_branch_factor, min_branch_factor, avg_branch_factor) = outgoing_branching_factor_calc(roads)
    (max_link_dist, min_link_dist, avg_link_dist) = __link_distances(roads)
    link_counter = __count_links(roads)
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    return {
        'Number of junctions': len(roads.junctions()),
        'Number of links': link_counter,
        'Outgoing branching factor': Stat(max=max_branch_factor, min=min_branch_factor, avg=avg_branch_factor),
        'Link distance': Stat(max=max_link_dist, min=min_link_dist, avg=avg_link_dist),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': collections.Counter(1 for x in range(15) for itr in roads.iterlinks() if itr.highway_type == x)
        # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))
        pass


if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
