# -----------------------------------------------------------
# heuristic.py 22/01/20
#
# Define heuristic functionality available throughout a project
#
# Copyright (c) 2020-2021 Team Artificial Incompetence, Comp 472
# All rights reserved.
# -----------------------------------------------------------
import constant


def get_heuristic(search_algorithm):
    """
    Get f(n), g(n) and h(n) node values for a particular algorithm
    :param (string) search_algorithm: type of the search algorithm
    :return: f(n), g(n) and h(n) values
    """
    fn = get_f_of_n(search_algorithm)
    gn = get_g_of_n(search_algorithm)
    hn = get_h_of_n(search_algorithm)
    return fn, gn, hn


def get_f_of_n(search_algorithm):
    """
    Get f(n) node value for a particular algorithm
    :param (string) search_algorithm: type of the search algorithm
    :return: f(n) value
    """
    if search_algorithm == constant.DFS:
        return 0


def get_g_of_n(search_algorithm):
    """
        Get g(n) node value for a particular algorithm
        :param (string) search_algorithm: type of the search algorithm
        :return: g(n) value
    """
    if search_algorithm == constant.DFS:
        return 0


def get_h_of_n(search_algorithm):
    """
        Get h(n) node value for a particular algorithm
        :param (string) search_algorithm: type of the search algorithm
        :return: h(n) value
    """
    if search_algorithm == constant.DFS:
        return 0
