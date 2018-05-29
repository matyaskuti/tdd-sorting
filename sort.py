def sort(list_):
    if len(list_) > 1:
        if list_[1] < list_[0]:
            list_[0], list_[1] = list_[1], list_[0]
    return list_
