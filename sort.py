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


def quick_sort(list_):
    if list_ == []:
        return list_
    lowest, middle, highest = _partition(list_)
    return [*quick_sort(lowest), middle, *quick_sort(highest)]


def _partition(list_):
    lowest, middle, highest = [], list_[0], []
    for i in list_[1:]:
        if i > middle:
            highest.append(i)
        else:
            lowest.append(i)

    return lowest, middle, highest
