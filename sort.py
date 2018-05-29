def sort(list_):
    for index in range(len(list_)-1):
        if _is_out_of_order(list_, index):
            _swap_with_next(list_, index)
    return list_


def _is_out_of_order(list_, index):
    return list_[index+1] < list_[index]


def _swap_with_next(list_, index):
    list_[index], list_[index+1] = list_[index+1], list_[index]
