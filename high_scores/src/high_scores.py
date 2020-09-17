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
