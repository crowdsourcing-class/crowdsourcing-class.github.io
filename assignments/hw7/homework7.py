############################################################
# NETS 213: Homework 7
############################################################

import pandas as pd

# Part 1 - Majority vote

def majority_vote(mturk_res):
    pass

def majority_vote_workers(mturk_res, votes):
    pass


# Part 1 - Weighted majority vote

def weighted_majority_vote_workers(mturk_res):
    pass

def weighted_majority_vote(mturk_res, workers):
    pass


# Part 2 - EM algorithm

def em_worker_quality(rows):
    pass

def em_votes(rows, worker_qual):
    pass

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(rows, mturk_res)
    return labels, worker_qual

def em_vote(rows, iter_num):
    pass


# Part 3 - Qualified workers

def select_qualified_worker(mturk_res):
    pass


# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('hw7_data.csv')

    # Call functions and output required CSV files
    pass

if __name__ == '__main__':
    main()
