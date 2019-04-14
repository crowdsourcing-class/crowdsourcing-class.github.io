############################################################
# NETS 213: Homework 7
############################################################

import pandas as pd
from collections import defaultdict

# Part 1 - Majority vote

adj_col_names = ['Input.adj_' + str(i) for i in range(1, 11)]
ans_col_names = ['Answer.adj_' + str(i) for i in range(1, 11)]
pos_qual_ans_col_names = ['Answer.pos_qual_ctrl_' + str(i) for i in range(1, 6)]

# Get the majority vote given a list of votes
def vote_majority(x):
    l = len(x) / 2
    c = 0
    for a in x:
        if a == 'Yes':
            c += 1
    if c >= l:
        return True
    else:
        return False

def majority_vote(mturk_res):
    col_names = ['Input.attr_id'] + adj_col_names + ans_col_names
    answers = [
        mturk_res[col_names].groupby(
            ['Input.attr_id'] + [adj_col_names[i]]
        )[ans_col_names[i]]
        .apply(list)
        .reset_index()
        .rename(index=str, columns={adj_col_names[i]:'adj', ans_col_names[i]:'ans'})
        for i in range(len(adj_col_names))]
    answers = pd.concat(answers, ignore_index=True)
    answers['ans'] = answers['ans'].apply(lambda x: vote_majority(x))
    answers = answers.rename(index=str, columns={'Input.attr_id':'attr_id','ans':'label'})
    answers = answers.sort_values(by=['attr_id', 'adj', 'label'])
    result = [tuple(x) for x in answers.values]
    return result

# Label vote as True if it is 'Yes'; 'False' if it's 'No' or 'Naa'
def label_vote(x):
    if x == 'Yes':
        return True
    else:
        return False

def check_vote(majority, worker):
    if majority == worker:
        return 1
    else:
        return 0

def majority_vote_workers(mturk_res, votes):
    label_dict = {(x,y):z for x, y, z in votes}

    answers = [
        mturk_res[['Input.attr_id', 'WorkerId'] + [adj_col_names[i]] + [ans_col_names[i]]]
        .apply(list)
        .rename(index=str, columns={'Input.attr_id':'attr_id', adj_col_names[i]:'adj', ans_col_names[i]:'ans'})
        for i in range(len(adj_col_names))]

    answers = pd.concat(answers, ignore_index=True)
    answers['ans'] = answers['ans'].apply(lambda x: label_vote(x))
    answers['correct'] = answers.apply(
                lambda x: int(label_dict[(x['attr_id'], x['adj'])] == x['ans']), 
                axis=1)
    answers['total'] = answers['ans'].apply(lambda x: 1)

    workers = answers.groupby('WorkerId').agg({'correct':sum, 'total':sum}).reset_index()
    workers['quality'] = workers.apply(
        lambda x: round(x['correct'] / x['total'], 3), 
        axis=1)
    workers = workers.drop(['correct', 'total'], axis=1)
    quality = sorted(tuple(x) for x in workers.values)

    return quality

# Part 1 - Weighted majority vote

def check_pos_qual(x):
    if x == 'Yes':
        return 1
    else:
        return 0

def weighted_majority_vote_workers(mturk_res):
    pos_ans = [
        mturk_res[['WorkerId'] + [pos_qual_ans_col_names[i]]]
        .apply(list)
        .rename(index=str, columns={pos_qual_ans_col_names[i]:'pos'})
        for i in range(len(pos_qual_ans_col_names))]
    pos_ans = pd.concat(pos_ans, ignore_index=True)
    pos_ans['correct'] = pos_ans['pos'].apply(lambda x:check_pos_qual(x))
    pos_ans = pos_ans.dropna()
    pos_ans = pos_ans.drop('pos', axis=1)

    neg_ans = mturk_res[['WorkerId', 'Answer.neg_qual_ctrl']] \
        .apply(list) \
        .rename(index=str, columns={'Answer.neg_qual_ctrl':'neg'})
    neg_ans['correct'] = neg_ans['neg'].apply(lambda x: 1 - check_pos_qual(x))
    neg_ans = neg_ans.dropna()
    neg_ans = neg_ans.drop('neg', axis=1)

    workers = pd.concat([pos_ans, neg_ans], ignore_index=True)
    workers['total'] = workers['WorkerId'].apply(lambda x: 1)

    workers = workers.groupby('WorkerId').agg({'correct':sum, 'total':sum}).reset_index()
    workers['quality'] = workers.apply(
        lambda x: round(x['correct'] / x['total'], 3), 
        axis=1)
    workers = workers.drop(['correct', 'total'], axis=1)
    quality = sorted(tuple(x) for x in workers.values)

    return quality

def vote_weight(worker_qual, ans, side):
    if ans == 'Yes':
        label = True
    else:
        label = False

    if label == side:
        return worker_qual
    else:
        return 0

def weighted_majority_vote(mturk_res, workers):
    quality = {w:q for (w, q) in workers}

    answers = [
        mturk_res[['Input.attr_id', 'WorkerId', 'Input.adj_' + str(i), 'Answer.adj_' + str(i)]]
        .rename(index=str, 
            columns={'Input.attr_id': 'attr_id', adj_col_names[i-1]:'adj', ans_col_names[i-1]:'ans'})
        for i in range(1, 11)
    ]
    answers = pd.concat(answers, ignore_index=True)

    # Compute votes and labels
    answers['yes'] = answers.apply(
        lambda x:vote_weight(quality[x['WorkerId']], x['ans'], True), axis=1)
    answers['no'] = answers.apply(
        lambda x:vote_weight(quality[x['WorkerId']], x['ans'], False), axis=1)
    answers = answers[['attr_id', 'adj', 'yes', 'no']].groupby(['attr_id', 'adj']).sum().reset_index()
    answers['label'] = answers.apply(lambda x:x['yes']>=x['no'], axis=1)
    answers = answers[['attr_id', 'adj', 'label']]
    answers = answers.sort_values(by=['attr_id', 'adj', 'label'])
    result = [tuple(x) for x in answers.values]
    return result


# Part 2 - EM algorithm

def em_votes(rows, worker_qual):
    url_votes = dict()
    for k in rows:
        if k[1] not in url_votes:
            url_votes[k[1]] = defaultdict(float)
        url_votes[k[1]]['porn'] += worker_qual[k[0]][(rows[k], 'porn')]
        url_votes[k[1]]['notporn'] += worker_qual[k[0]][(rows[k], 'notporn')]
    
    labels = dict()
    for k in url_votes:
        if url_votes[k]['porn'] >= url_votes[k]['notporn']:
            labels[k] = 'porn'
        else:
            labels[k] = 'notporn'
    return labels

def em_worker_quality(rows, labels):
    num_porn = 0
    num_notporn = 0
    for l in labels:
        if labels[l] == 'porn':
            num_porn += 1
        else:
            num_notporn += 1

    worker_qual = dict()    
    for k in rows:
        if k[0] not in worker_qual:
            worker_qual[k[0]] = dict()
            worker_qual[k[0]][('porn', 'porn')] = 0
            worker_qual[k[0]][('porn', 'notporn')] = 0
            worker_qual[k[0]][('notporn', 'porn')] = 0
            worker_qual[k[0]][('notporn', 'notporn')] = 0
        # Count new number of "correct" answers
        worker_qual[k[0]][(labels[k[1]], rows[k])] += 1

    for w in worker_qual:
        worker_qual[w][('porn', 'porn')] /= num_porn
        worker_qual[w][('porn', 'notporn')] /= num_porn
        worker_qual[w][('notporn', 'porn')] /= num_notporn
        worker_qual[w][('notporn', 'notporn')] /= num_notporn
    
    return worker_qual

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(rows, labels)
    return labels, worker_qual

def em_vote(rows, iter_num):
    init_labels = {(x, y): z for x, y, z in rows.values}
    workers = list(rows.groupby('worker').apply(list).reset_index()['worker'])
    worker_qual = dict()
    for w in workers:
        worker_qual[w] = dict()
        worker_qual[w][('porn', 'porn')] = 1
        worker_qual[w][('porn', 'notporn')] = 0
        worker_qual[w][('notporn', 'porn')] = 0
        worker_qual[w][('notporn', 'notporn')] = 1

    for i in range(iter_num):
        labels, worker_qual = em_iteration(init_labels, worker_qual)
        print("Iteration", i + 1,"Labels:")
        for l in labels:
            print(l, labels[l])
        print()

        print("Iteration", i + 1,"Worker quality:")
        for w in worker_qual:
            print(w, worker_qual[w])
        print('-----')

    labels = sorted(labels.items())
    return labels


# Part 3 - Qualified workers

def filter_pos_qual_control(row):
    yes = sum(1 if row[pos_qual_ans_col_names[i]] == 'Yes' else 0 
        for i in range(len(pos_qual_ans_col_names)))
    if yes >= 4:
        return 1
    else:
        return 0

def select_qualified_worker(mturk_res):
    workers = mturk_res.groupby('WorkerId').apply(len).reset_index(name="count")
    workers = set(x for x, y in workers[workers['count'] >= 5].values)

    filtered = mturk_res[mturk_res['WorkerId'].isin(workers)]
    counts = filtered.groupby('WorkerId').apply(len).reset_index(name="total")
    filtered = filtered[filtered['Answer.neg_qual_ctrl'] != 'Yes']

    filtered = filtered[['WorkerId'] + pos_qual_ans_col_names]
    filtered['good'] = filtered.apply(lambda x:filter_pos_qual_control(x[pos_qual_ans_col_names]), axis=1)
    filtered = filtered.drop(pos_qual_ans_col_names, axis=1)
    filtered = filtered.groupby('WorkerId').sum().reset_index()
    filtered['total'] = counts['total']
    filtered['quality'] = filtered.apply(lambda x:round(x['good']/x['total'], 3), axis=1)
    filtered = filtered[filtered['quality'] >= 0.75]
    filtered = filtered.drop(['good', 'total'], axis=1)

    qualified = sorted(tuple(x) for x in filtered.values)
    return qualified


# Your main function

def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('hw7_data.csv')

    # Call functions and output required CSV files
    mv = majority_vote(mturk_res)
    output1 = pd.DataFrame(mv, columns=['attr_id', 'adj', 'label'])
    output1.to_csv('output1.csv', index=False)

    mvw = majority_vote_workers(mturk_res, mv)
    output2 = pd.DataFrame(mvw, columns=['worker_id', 'quality'])
    output2.to_csv('output2.csv', index=False)

    wmvw = weighted_majority_vote_workers(mturk_res)
    output3 = pd.DataFrame(wmvw, columns=['worker_id', 'quality'])
    output3.to_csv('output3.csv', index=False)

    wmv = weighted_majority_vote(mturk_res, wmvw)
    output4 = pd.DataFrame(wmv, columns=['attr_id', 'adj', 'label'])
    output4.to_csv('output4.csv', index=False)

    toy_data = pd.read_csv(
        'em_toy_data.txt', delimiter='\t', names=['worker', 'url', 'label'])
    em_labels = em_vote(toy_data, 3)
    output5 = pd.DataFrame(em_labels, columns=['url', 'label'])
    output5.to_csv('output5.csv', index=False)

    qw = select_qualified_worker(mturk_res)
    output6 = pd.DataFrame(qw, columns=['worker_id', 'percentage'])
    output6.to_csv('output6.csv', index=False)

if __name__ == '__main__':
    main()
