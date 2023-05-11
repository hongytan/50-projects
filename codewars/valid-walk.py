def is_valid_walk(walk):
    opposite = {'n':'s', 'e':'w', 'w':'e', 's':'n'}
    if len(walk) != 10:
        return False
    while walk:
        dir = walk[0]
        if opposite[dir] in walk[1:]:
            walk.pop(0)
            walk.remove(opposite[dir])
        else:
            return False
    return True

# Best Solution
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')