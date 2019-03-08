def electionWinner(votes):
    res ={}
    for cand in votes:
        res[cand]=res.get(cand,0)+1

    maxVotes = max(res.values())
    maxCands = [x for (x,y) in res.items() if y==maxVotes]
    maxCands.sort()
    return maxCands[-1]

input = ['Trump','Trump','Harry','Alex','Mary','Mary','Alex']
print(electionWinner(input))