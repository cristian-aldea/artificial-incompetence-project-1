# -----------------------------------------------------------
# dfs.py 22/01/20
#
# Define and run depth-first search algorithm
#
# Copyright (c) 2020-2021 Team Artificial Incompetence, COMP 472
# All rights reserved.
# -----------------------------------------------------------
import time

import constant
from utils import *
from utils import get_puzzle_info


def main(file_path):
    """
    Read file, retrieve puzzle info, and execute dfs for each puzzle
    :param (string) file_path: relative path to the input file
    :return: void
    """
    prepare_performance_file(DFS_ALGORITHM, NO_HEURISTIC)
    with open(file_path) as fp:
        for puzzle_number, puzzle in enumerate(fp):
            max_d, max_l, grid, goal = get_puzzle_info(puzzle)
            execute_dfs(grid, max_d, goal, puzzle_number)


def execute_dfs(grid, max_d, goal, puzzle_number):
    """
    Wrapper for DFS
    :param (ndarray) grid: numpy 2-D array representation of the input board
    :param (int) max_d: maximum depth
    :param (string) goal: serialized goal grid
    :param (int) puzzle_number: line number of the puzzle for which DFS is executed
    :return: void
    """
    print('Execute DFS with max depth {} on grid \n{} '.format(max_d, grid))
    open_list = []
    open_set = set()
    closed_dict = {}
    search_path = []

    s_grid = grid_to_string(grid)
    path_to_root = ['{}   {}'.format(0, s_grid)]

    root = Node(grid, s_grid, 1, path_to_root)
    open_list.append(root)
    open_set.add(s_grid)
    start_time = time.time()
    solution_path = dfs(open_list, open_set, closed_dict, search_path, goal, max_d,
                        start_time + TIME_TO_SOLVE_PUZZLE_SECONDS)
    end_time = time.time()
    write_results(puzzle_number, DFS_ALGORITHM, NO_HEURISTIC, solution_path, search_path)
    gather_performance(puzzle_number, np.size(grid, 0), solution_path, len(search_path),
                       start_time, end_time, DFS_ALGORITHM, NO_HEURISTIC)
    print('Found no solution' if solution_path == constant.NO_SOLUTION
          else 'Found result in {} moves'.format(len(solution_path) - 1))


def dfs(open_list: List[Node], open_set, closed_dict, search_path, goal, max_d, allowed_execution_time):
    """
    Iterative DFS.
    Each node in the open list carries: grid, level and a solution_path up to this grid
    :param (stack) open_list: stack of yet to be processed grids
    :param (set) open_set: keep track of the configurations in the open_list
    :param (dictionary) closed_dict: visited grid configurations and their depth
    :param (list) search_path: path up to the specific node
    :param (string) goal: goal configuration
    :param (int) max_d: maximum execution depth
    :param allowed_execution_time: maximum time to solve a puzzle
    :return (list | string): path up to identified solution. List of paths or 'no solution'
    """
    while len(open_list) > 0:
        node = open_list.pop()

        open_set.remove(node.s_grid)
        closed_dict[node.s_grid] = node.depth
        search_path.append(get_search_move(constant.DFS_ALGORITHM, node))
        if node.s_grid == goal:
            return node.path_from_root
        if node.depth < max_d:
            evaluate_dfs_children(open_list, open_set, closed_dict, node)
        if time.time() >= allowed_execution_time:
            return constant.NO_SOLUTION
    return constant.NO_SOLUTION


# Define input file here
main('input.txt')
