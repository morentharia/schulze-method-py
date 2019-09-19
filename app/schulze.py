import numpy as np
import pandas as pd
from itertools import chain, permutations


def schulze_method(data):
    candidates = (c for v in data for c in chain.from_iterable(v.get("ballot", [])))
    candidates = sorted(list(set(candidates)))

    # compute pairwise preferences
    pref = pd.DataFrame(
        np.zeros((len(candidates), len(candidates))),
        index=candidates, columns=candidates,
        dtype=int,
    )
    for d in data:
        count, ballot = d.get("count", 0), d.get("ballot", [])
        for i in range(len(ballot)-1):
            winners, loosers = ballot[i], list(chain.from_iterable(ballot[i+1:]))
            pref.loc[winners, loosers] += count

    for i, j in permutations(candidates, 2):
        if pref.loc[i, j] < pref.loc[j, i]:
            pref.loc[i, j] = 0

    # compute the strongest path strengths
    for k, i, j in permutations(candidates, 3):
        pref.loc[i, j] = max(pref.loc[i, j], min(pref.loc[i, k], pref.loc[k, j]))

    # ranking candidates
    for i, j in permutations(candidates, 2):
        if pref.loc[i, j] < pref.loc[j, i]:
            pref.loc[i, j] = 0

    pref = pref.applymap(lambda x: x > 0).apply(sum, axis=1)
    grouped = pref.groupby(pref)
    result = grouped.apply(lambda x: x.index.tolist())[::-1].tolist()
    return result
