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

def em_worker_quality(rows, labels):
    # the return format should be a dict that maps
    # key: 'workerX'
    # value: {('fakenews', 'fakenews'): A, ('fakenews', 'notfakenews'): B, ('notfakenews', 'fakenews'): C, ('notfakenews', 'notfakenews'): D}
    # where X is a worker index, and A, B, C, D are values between 0.0 and 1.0
    pass

def em_votes(rows, worker_qual):
    pass

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(rows, labels)
    return labels, worker_qual

def em_vote(rows, iter_num):
    
    # return both the final labels and the final worker qualities
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
