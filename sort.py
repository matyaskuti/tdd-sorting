def sort(list_):
    index = 0
    while len(list_) > index+1:
        if _is_out_of_order(list_, index):
            _swap_with_next(list_, index)
        index += 1
    return list_


def _is_out_of_order(list_, index):
    return list_[index+1] < list_[index]


def _swap_with_next(list_, index):
    list_[index], list_[index+1] = list_[index+1], list_[index]
