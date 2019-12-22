def get_combinations(seq: set) -> []:
    res = []
    for i in seq:
        if len(seq) > 1:
            seq_copy = seq.copy()
            seq_copy.remove(i)
            for part in get_combinations(seq_copy):
                res.append([i] + part)
        else:
            res.append([i])
    return res

