def bubble_sort(list_):
    for length in range(len(list_), 1, -1):
        for index in range(length-1):
            if _is_out_of_order(list_, index):
                _swap_with_next(list_, index)
    return list_


def _is_out_of_order(list_, index):
    return list_[index+1] < list_[index]


def _swap_with_next(list_, index):
    list_[index], list_[index+1] = list_[index+1], list_[index]


def sort(list_):
    sorted_ = []
    if len(list_) <= 1:
        return list_
    else:
        lowest = 0
        middle = list_[0]
        highest = 0
        for i in list_:
            if i > middle:
                highest = i
            if i < middle:
                lowest = i

        sorted_.append(lowest)
        sorted_.append(middle)
        sorted_.append(highest)
    return sorted_
