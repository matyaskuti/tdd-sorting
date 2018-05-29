def sort(list_):
    index = 0
    while len(list_) > index+1:
        if list_[index+1] < list_[index]:
            _swap_with_next(list_, index)
        index += 1
    return list_


def _swap_with_next(list_, index):
    list_[index], list_[index+1] = list_[index+1], list_[index]
