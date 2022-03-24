import numpy as np

def helper(method, ls):
    row = list(method(ls, axis=0))
    column = list(method(ls, axis=1))
    total = float(method(ls))
    return [row, column, total]

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    ls = np.array(list).reshape(3,3)
    res = {}
    res['mean'] = helper(np.mean, ls)
    res['variance'] = helper(np.var, ls)
    res['standard deviation'] = helper(np.std, ls)
    res['max'] = helper(np.max, ls)
    res['min'] = helper(np.min, ls)
    res['sum'] = helper(np.sum, ls)
    return res
