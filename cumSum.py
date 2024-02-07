def cum_sum(lst, i=None):
    if i is None:
        i = len(lst) - 1

    if i == 0:
        return [lst[0]]

    r = cum_sum(lst, i - 1)
    c = lst[i] + r[0]

    return [c] + r


li = [1, 2, 3, 4, 5]
res = []
res.extend(cum_sum(li))
# res.reverse()
print(res)
