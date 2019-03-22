############################################################
# NETS 213: Homework 7
############################################################


# Part 1 - Majority vote

def majority_vote(rows):
    pass

def majority_vote_workers(rows, votes):
    pass


# Part 1 - Weighted majority vote

def weighted_majority_vote_workers(rows):
    pass

def weighted_majority_vote(rows, workers):
    pass


# Part 2 - EM algorithm

def em_worker_quality(rows):
    pass

def em_votes(rows, worker_qual):
    pass

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(labels, rows)
    return labels, worker_qual

def em_vote(rows, iter_num):
    pass


# Part 3 - Qualified workers

def select_qualified_worker(rows):
    pass


# Your main function

def main():
    # Call above functions and output required CSV files
    pass

if __name__ == '__main__':
    main()
