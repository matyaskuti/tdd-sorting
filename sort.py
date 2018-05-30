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
    if list_[0] > list_[1]:
        sorted_.append(list_[1])
        sorted_.append(list_[0])
    else:
        sorted_.append(list_[0])
        sorted_.append(list_[1])
    return sorted_
