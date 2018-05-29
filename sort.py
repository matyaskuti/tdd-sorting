def sort(list_):
    for length in range(len(list_), 1, -1):
        for index in range(length-1):
            if _is_out_of_order(list_, index):
                _swap_with_next(list_, index)
    return list_


def _is_out_of_order(list_, index):
    return list_[index+1] < list_[index]


def _swap_with_next(list_, index):
    list_[index], list_[index+1] = list_[index+1], list_[index]
