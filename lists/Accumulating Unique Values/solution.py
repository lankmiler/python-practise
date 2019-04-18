from numpy import unique

values = [1, 2, 3, 4, 4, 5, 6, 6, 7]


def accumulate(lst):
    result = list()
    for v in lst:
        if v not in result:
            result.append(v)
    return result


def accumulate_using_set(lst):
    return list(set(lst))


def accumulate_using_numpy(lst):
    return unique(lst)