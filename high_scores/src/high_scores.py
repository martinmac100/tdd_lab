def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    length_of_list = len(scores)
    top_three = scores[length_of_list - 3:]
    return top_three

def highest_to_lowest(scores):
    scores.sort()
    scores.reverse()
    return scores

def top_three_tie(tied_scores):
    tied_scores.sort()
    length_of_list = len(tied_scores)
    top_three = tied_scores[length_of_list - 3:]
    return top_three
