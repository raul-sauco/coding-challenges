# https://www.codewars.com/kata/554910d77a3582bbe300009c/train/python

from collections import defaultdict


def get_winner(ballots):
    # default dict with 0
    votes = defaultdict(int)
    current_winner = None
    for ballot in ballots:
        # Add the current vote to the candidate
        votes[ballot] += 1
        # If the candidate has more votes than the current winner, store it
        # as the current winner
        if votes[ballot] > votes[current_winner]:
            current_winner = ballot
    # Return the current winner if it has more than half the votes
    return current_winner if votes[current_winner] > len(ballots) / 2 else None
